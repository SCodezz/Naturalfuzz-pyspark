# 🧪 NaturalFuzz – Semantic-Aware Data Fuzzing in PySpark 🧠

A **simplified PySpark implementation** of **NaturalFuzz**, based on the ASE 2023 paper by Humayun, Wu, Kim & Gulzar:
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
BigFuzz      | 4        | 1      |   0.0%

NaturalFuzz achieves max coverage, correctly detects the fault, and preserves full naturalness—demonstrating its effectiveness.

##📂 Project Structure
Naturalfuzz-pyspark/
├── naturalfuzz_colab.ipynb     # Colab demo notebook
├── naturalfuzz_comparison.py   # Standalone PySpark script
└── README.md                   # This file







  















[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SCodezz/naturalfuzz-pyspark/blob/main/naturalfuzz_colab.ipynb)
