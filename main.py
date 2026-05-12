import json
from loader import load_excel
from column_mapper import detect_columns
from rules_engine import run_rule
from report_writer import write_reports

# Load data
df = load_excel("sample_Row_Data.xlsx")

# Detect columns
col_map = detect_columns(df)

print("Detected Columns:", col_map)

# Load rules
with open("rules.json") as f:
    rules = json.load(f)

all_results = {}

# Run rules
for rule in rules:
    result = run_rule(df, rule, col_map)
    all_results[rule["rule_name"]] = result

# Write output
write_reports(all_results, "output_report.xlsx")

print("DONE - Report Generated")
