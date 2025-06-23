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
   A sample sales table with one row containing a **positive discount** (i.e., `discount > 0`).

2. **Branch Profiling**  
   Columns added to simulate decision paths:
   
   - `branch_november` → month == November  
   - `branch_high_value` → price > 250  
   - `branch_item_A`     → item_id == 101  

3. **NaturalFuzz Mutation**  
   Applies semantic-aware mutations to ~30–70% of rows—from valid “donor” rows—while preserving the injected faulty record.

4. **Evaluation Metrics**  
   - ✅ **Coverage**: number of unique branch flag combinations  
   - ✅ **Fault Detection**: presence of row(s) with `discount > 0`  
   - ✅ **Naturalness**: fraction of realistic (schema-valid) values  

5. **Baseline Comparison**  
   Compare NaturalFuzz with:

   - **Jazzer** (random mutations)  
   - **BigFuzz** (schema-aware but extreme mutations)

---

## 📊 Example Output

```text
=== Evaluation Metrics ===

Tool         | Coverage | Faults | Naturalness
----------------------------------------------
NaturalFuzz  | 4        | 2      | 100.0%
Jazzer       | 3        | 0      | 80.0%
BigFuzz      | 4        | 1      | 0.0%
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

## 🧪 How to Use It Locally/Ubuntu:

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


