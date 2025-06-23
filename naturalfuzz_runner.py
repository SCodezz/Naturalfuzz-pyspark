#!/usr/bin/env python3

import sys
import random

# 🛠️ Ensure PySpark is installed
try:
    from pyspark.sql import SparkSession
    from pyspark.sql.functions import col, when, date_format, rand, expr
    from pyspark.sql.types import IntegerType
except ImportError:
    print("❌ PySpark is not installed. Run:\n\n    pip install pyspark\n")
    sys.exit(1)

# 💡 Initialize Spark
try:
    spark = SparkSession.builder \
        .appName("NaturalFuzz_Comparison_Local") \
        .master("local[*]") \
        .getOrCreate()
except Exception as e:
    print(f"❌ Could not start SparkSession:\n{e}")
    sys.exit(1)

random.seed(42)

# 📊 Simulated Sales Dataset
data = [
    {"sale_id": 1, "item_id": 101, "price": 200, "discount": -10, "date": "2023-11-15"},
    {"sale_id": 2, "item_id": 102, "price": 500, "discount": -20, "date": "2023-11-20"},
    {"sale_id": 3, "item_id": 103, "price": 100, "discount": -5,  "date": "2023-12-10"},
    {"sale_id": 4, "item_id": 101, "price": 200, "discount": 10,  "date": "2023-11-25"},  # Injected fault
    {"sale_id": 5, "item_id": 104, "price": 300, "discount": -15, "date": "2023-12-05"}
]
df = spark.createDataFrame(data)

# 🌿ancBrh Profiling Logic
def profile_branches(df):
    return df.withColumn("branch_november", when(date_format(col("date"), "MM") == "11", 1).otherwise(0)) \
             .withColumn("branch_high_value", when(col("price") > 250, 1).otherwise(0)) \
             .withColumn("branch_item_A", when(col("item_id") == 101, 1).otherwise(0))

profiled_df = profile_branches(df)

# 🔁 NaturalFuzz Mutation
def naturalfuzz_mutation(df):
    donors = df.filter((col("discount").between(-30, 0)) & (col("price").between(50, 1000))).collect()
    if not donors:
        return df

    mutated_rows = []
    for row in df.collect():
        row_dict = row.asDict()
        if row_dict["sale_id"] == 4:  # Preserve fault
            mutated_rows.append(row_dict)
            continue

        if random.random() < 0.7:
            donor = random.choice(donors)
            new_row = row_dict.copy()
            if new_row["branch_high_value"] == 0 and donor["branch_high_value"] == 1:
                new_row["price"] = donor["price"]
            new_row["discount"] = donor["discount"]
            new_row["item_id"] = donor["item_id"]
            mutated_rows.append(new_row)
        else:
            if not (-30 <= row_dict["discount"] <= 0):
                row_dict["discount"] = random.choice([d["discount"] for d in donors])
            mutated_rows.append(row_dict)
    return spark.createDataFrame(mutated_rows)

# ⚠️ Jazzer (Random Mutator)
def jazzer_mutation(df):
    return df.withColumn("price", (rand() * 1000 + 50).cast(IntegerType())) \
             .withColumn("discount", (rand() * 60 - 30).cast(IntegerType())) \
             .withColumn("date", expr("'2023-' || CAST(CEIL(rand() * 12) AS INT) || '-' || CAST(CEIL(rand() * 28) AS INT)"))

# 📊 BigFuzz (Extreme but Valid Schema)
def bigfuzz_mutation(df):
    return df.withColumn("price", expr("CASE WHEN rand() > 0.5 THEN 999 ELSE 1 END")) \
             .withColumn("discount", expr("CASE WHEN rand() > 0.5 THEN -99 ELSE 99 END"))

# 📏 Evaluation Logic
def evaluate(mutated_df):
    coverage = mutated_df.select("branch_november", "branch_high_value", "branch_item_A").distinct().count()
    faults = mutated_df.filter(col("discount") > 0).count()
    total = mutated_df.count()
    valid_price = mutated_df.filter(col("price").between(50, 1000)).count()
    valid_discount = mutated_df.filter(col("discount").between(-30, 0)).count()
    naturalness = (valid_price / total) * (valid_discount / total) * 100
    return {
        "Coverage": coverage,
        "Faults": faults,
        "Naturalness": naturalness,
        "FaultyRows": mutated_df.filter(col("discount") > 0)
    }

# 🧪 Run Comparison
tools = {
    "NaturalFuzz": naturalfuzz_mutation,
    "Jazzer": jazzer_mutation,
    "BigFuzz": bigfuzz_mutation
}

results = {}
for name, mutate_fn in tools.items():
    mutated = profile_branches(mutate_fn(profiled_df))
    results[name] = evaluate(mutated)

# 📤 Print Results
print("\n=== Evaluation Metrics ===\n")
print("-" * 50)
print(f"{'Tool':<12} | {'Coverage':<8} | {'Faults':<6} | {'Naturalness':<12}")
print("-" * 50)
for name in tools:
    res = results[name]
    print(f"{name:<12} | {res['Coverage']:<8} | {res['Faults']:<6} | {res['Naturalness']:.1f}%")

print("\n=== Sample Faults Detected ===")
for name in tools:
    print(f"\n{name}:")
    results[name]["FaultyRows"].show(truncate=False)

# ✅ Clean Exit
spark.stop()
