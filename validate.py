
import pandas as pd
import argparse
import os
import sys

REQUIRED_COLUMNS = ["transaction_id", "amount", "status", "date"]

def ensure_dir(path):
    if os.path.exists(path) and not os.path.isdir(path):
        os.remove(path)
    os.makedirs(path, exist_ok=True)

def load_data(file_path):
    if not os.path.exists(file_path):
        print("Input file not found")
        sys.exit(1)
    return pd.read_csv(file_path)

def validate_columns(df):
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        print(f"Missing required columns: {missing}")
        sys.exit(1)

def clean_data(df):
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()
    return df

def validate_data(df):
    errors = []
    for index, row in df.iterrows():
        if row["amount"] < 0:
            errors.append((index + 1, "Negative amount"))
        if row["status"] not in ["SUCCESS", "FAILED"]:
            errors.append((index + 1, "Invalid status"))
        if pd.isna(row["date"]):
            errors.append((index + 1, "Date missing"))
        else:
            try:
                pd.to_datetime(row["date"])
            except ValueError:
                errors.append((index + 1, "Invalid date format"))
    return errors

def write_report(errors, outdir):
    ensure_dir(outdir)
    path = os.path.join(outdir, "errors.csv")
    pd.DataFrame(errors, columns=["row_number", "error"]).to_csv(path, index=False)
    print(f"Report generated: {path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--outdir", default="reports")
    args = parser.parse_args()
    df = load_data(args.file)
    validate_columns(df)
    df = clean_data(df)
    errors = validate_data(df)
    write_report(errors, args.outdir)
    print(f"Validation completed. Total errors: {len(errors)}")

if __name__ == "__main__":
    main()
