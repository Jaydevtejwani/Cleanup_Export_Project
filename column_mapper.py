import re

COLUMN_PATTERNS = {
    "SSN": [r"\bssn\b", r"social", r"security"],
    "DOB": [r"\bdob\b", r"birth", r"date.*birth"],
    "Full Name": [r"name", r"full.*name", r"customer", r"person"],
    "DL": [r"dl\b", r"driving", r"license"],
    "Passport": [r"passport"],
    "Phone": [r"phone", r"mobile", r"contact"],
    "Address": [r"address", r"addr"],
    "ITIN": [r"\bitin\b"],
    "PAN": [r"\bpan\b"],
    "MRN": [r"\bmrn\b", r"medical", r"record"]
}

def detect_columns(df):
    mapping = {}

    for col in df.columns:
        col_lower = col.lower()

        for key, patterns in COLUMN_PATTERNS.items():
            for p in patterns:
                if re.search(p, col_lower):
                    mapping[key] = col
                    break

    return mapping