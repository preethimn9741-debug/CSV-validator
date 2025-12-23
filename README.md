# CSV-validator
# CSV Data Validator

## 📌 Project Description
**CSV Data Validator** is a Python-based command-line tool that validates CSV files against configurable rules.
It checks for missing or incorrect columns, invalid values, incorrect data types, and formatting issues, then generates a detailed error report.

This project is built as a **learning and practice tool** to understand data quality validation and data cleaning workflows commonly used in data engineering.

---

## 🎯 Purpose of the Project
This project is:
- ✅ A learning exercise  
- ✅ A reusable CSV validation utility  
- ❌ Not a production-grade validation framework  

It helps ensure CSV data meets expected quality standards before further processing.

---

## 🛠 Tech Stack
- **Language:** Python  
- **Library:** pandas  
- **Execution:** Command Line (CLI)  
- **Input Format:** CSV  
- **Output Format:** CSV  

---

## 🏗 Architecture Overview
- CSV files are read using pandas
- Column names are normalized (case- and space-neutral)
- Validation rules define required columns and constraints
- Data is cleaned before validation
- Validation errors are collected and written to a CSV report

---

## 📂 Project Structure

---

## ⚙️ Installation Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd csv_validator
