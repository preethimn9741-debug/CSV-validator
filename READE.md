# CSV Validation Project

This project validates CSV files and generates a detailed error report.  
It is designed to be extensible and suitable for real-world data quality checks.

---

## Features

### Core Features
- Validates required columns
- Detects negative numeric values
- Validates allowed status values
- Checks missing and invalid date formats
- Cleans leading and trailing spaces in string columns
- Generates an error report in CSV format

### Additional Features
- Command-line interface (CLI) for flexible execution
- Automatic creation of output directory
- Case-insensitive column name validation
- Clear error messages for missing files and schema issues
- Modular code structure for easy extension
- Ready for configuration-based rules (future enhancement)
- Can be extended for multiple datasets

---

## Project Files
project/
│
├── validate.py # CSV validation script

├── input.csv # Input CSV file

├── reports/

│ └── errors.csv # Generated validation report

├── README.md # Documentation


---

## Validation Rules
The validator checks:
- Required columns:
  - `transaction_id`
  - `amount`
  - `status`
  - `date`
- `amount` must not be negative
- `status` must be `SUCCESS` or `FAILED`
- `date` must be present and valid
- Extra spaces in string fields are removed before validation

## How to Run

python validate.py --file input.csv --outdir reports

Output

A CSV error report is generated at:

reports/errors.csv

Example Output (errors.csv)
row_number,error
2,Negative amount
3,Invalid date format

Conclusion

This project provides a practical CSV validation framework that can be used for learning, testing, and data quality checks.
It is suitable for backend, data engineering, and interview demonstration purposes.




