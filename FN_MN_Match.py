import pandas as pd

# Load Excel
df = pd.read_excel("Data.xlsx")

# Clean columns (NaN safe)
df["First Name"] = df["First Name"].fillna("").astype(str).str.strip().str.title()
df["Middle Name"] = df["Middle Name"].fillna("").astype(str).str.strip().str.title()
df["Last Name"] = df["Last Name"].fillna("").astype(str).str.strip().str.title()

# Step 1: Combined = First + Middle (no space)
df["Combined"] = (df["First Name"] + df["Middle Name"]).str.strip()

# Step 2: Short name (last character removed safely)
df["ShortName"] = df["Combined"].apply(lambda x: x[:-1] if len(x) > 0 else "")

# -------------------------------
# LOGIC IMPLEMENTATION
# -------------------------------

result_rows = []

for i in range(len(df)):

    combined_name = df.loc[i, "Combined"]
    short_name = df.loc[i, "ShortName"]
    last_name = df.loc[i, "Last Name"]

    if combined_name == "":
        continue

    # Step 1: Find Combined name in First Name column
    match1 = df[
        (df["First Name"] == combined_name) &
        (df["Last Name"] == last_name)
    ]

    if not match1.empty:

        # Step 2: Find Short name in First Name column
        match2 = df[
            (df["First Name"] == short_name) &
            (df["Last Name"] == last_name)
        ]

        if not match2.empty:
            result_rows.append(match1.iloc[0])
            result_rows.append(match2.iloc[0])

# Final Output
result_df = pd.DataFrame(result_rows).drop_duplicates()

result_df.to_excel("Cheks.xlsx",index=False)
