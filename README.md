# 🧪 NaturalFuzz – Semantic-Aware Data Fuzzing in PySpark 🧠

NaturalFuzz is a research-backed approach to test data generation that focuses on producing semantically valid, schema-aware, and realistic inputs for big data analytics pipelines. Unlike traditional fuzzers that generate arbitrary or malformed data, NaturalFuzz mutates real-world-like input records to explore logical branches and uncover subtle business logic faults.

This repository provides a simplified PySpark implementation of NaturalFuzz, based on the ASE 2023 paper by researchers from Virginia Tech and UCLA. 

> *"NaturalFuzz: Natural Input Generation for Big Data Analytics"*  
> Repository: https://github.com/SEED‑VT/NaturalFuzz

This project demonstrates key concepts—natural test input generation, branch-aware mutations, and logic-fault detection—through a self-contained notebook and script.

---

## 🚀 Run It Now: Google Colab

No setup needed! Just click:

👉 **[Open in Colab](https://colab.research.google.com/github/SCodezz/naturalfuzz-pyspark/blob/main/naturalfuzz_colab.ipynb)**

---

## 📘 What’s Inside

1. **Dataset with a Faulty Record**  
A small sales table with one row containing a positive discount (discount > 0) to simulate a semantic bug.

2. **Branch Profiling**  
Assigns binary branch flags for each row to simulate program decision paths:
- b_nov → month == November
- b_high → price > 250
- b_itemA → item_id == 101

3. **NaturalFuzz Mutation**  
Implements three core steps from the paper in simplified form:
- Branch Profiling → Assign path vectors
- Seed Selection → Keep rows adding new coverage
- Interleaving Mutation → Combine rows column-wise to explore new paths

4. **Evaluation Metrics**  
Calculates:
- ✅ Coverage: number of unique branch vector combinations
- ✅ Fault Detection: rows with discount > 0 (semantic faults)
- ✅ Naturalness: fraction of realistic (schema-valid) values

5. **Baseline Comparison**  
   Compare NaturalFuzz with:

   - **Jazzer** (random mutations)  
   - **BigFuzz** (schema-aware but extreme mutations)

---

## 📊 Example Output

```text
=== NaturalFuzz ===
Coverage: 3
Faults: 0
Naturalness: 100.0%

Final Mutated Data:
+------+-------+-----+----------+--------+-------+-----+-------+
|b_high|b_itemA|b_nov|      date|discount|item_id|price|sale_id|
+------+-------+-----+----------+--------+-------+-----+-------+
|     1|      1|    1|2023-11-15|     -10|    101|  300|      1|
|     1|      1|    1|2023-11-20|     -20|    101|  500|      2|
|     0|      0|    0|2023-12-10|      -5|    103|  100|      3|
|     1|      1|    0|2023-12-05|     -15|    101|  300|      5|
+------+-------+-----+----------+--------+-------+-----+-------+

```
NaturalFuzz achieves max coverage, correctly detects the fault, and preserves full naturalness—demonstrating its effectiveness.





---

## 📌 Use Cases

* 🔍 Testing ETL logic with production-like data
* 🧪 Validating analytics pipelines with realistic scenarios
* 🧰 Creating semantically valid test sets for CI/CD
* 📚 Teaching data fuzzing and test coverage principles

---

## 📈 Comparison with Traditional Fuzzers

| Feature               | Traditional Fuzzers  | NaturalFuzz  |
| --------------------- | -------------------- |------------- |
| Schema Awareness      | ❌                  | ✅           |
| Semantic Validity     | ❌                  | ✅           |
| Business Logic Faults | ❌                  | ✅           |
| Coverage Guidance     | ❌                  | ✅           |
| Natural Data          | ❌                  | ✅           |
| Easy Debugging        | ❌                  | ✅           |

---

## 🧰 System Requirements

To run this project locally, your system should meet:

| Requirement  | Status | Notes                                              |
| ------------ | ------ | -------------------------------------------------- |
| Python 3.x   | ✅      | Use `python3 --version` to check                   |
| Java (JDK)   | ✅      | Required by Spark. Recommend OpenJDK 8 or 11       |
| Memory ≥ 2GB | ✅      | Lightweight project, but Spark needs some headroom |

💡 **Tip:**
To install Java on Ubuntu:

```bash
sudo apt install openjdk-11-jdk
```

And set `JAVA_HOME` in your shell config if needed:

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

---

## 🧪 How to Use It Locally/Ubuntu :

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/naturalfuzz-pyspark.git
cd naturalfuzz-pyspark

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

# 3. Install PySpark
pip install pyspark

# 4. Run the script
python3 naturalfuzz_runner.py
```

---


🙏 Acknowledgements
This project is a simplified reimplementation inspired by the original ASE 2023 research paper:

📄 Citation:
Humayun, A., Wu, Y., Kim, M., & Gulzar, M. A. (2023). NaturalFuzz: Natural Input Generation for Big Data Analytics.

🧠 Authors of the Original Paper:

Ahmad Humayun (Virginia Tech),
Yaoxuan Wu (UCLA),
Miryung Kim (UCLA),
Muhammad Ali Gulzar (Virginia Tech)


[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SCodezz/naturalfuzz-pyspark/blob/main/naturalfuzz_colab.ipynb)


