import pandas as pd

# Load Excel
df = pd.read_excel("Data.xlsx")

# ---------------------------------
# CLEAN COLUMNS
# ---------------------------------
for col in ["First Name", "Middle Name", "Last Name"]:
    df[col] = (
        df[col]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.title()
    )

# ---------------------------------
# CREATE COMBINED + SHORT NAME
# ---------------------------------

# Combined = First + Middle
df["Combined"] = (
    df["First Name"] + df["Middle Name"]
).str.strip()

# ShortName = remove last character
df["ShortName"] = df["Combined"].apply(
    lambda x: x[:-1] if len(x) > 0 else ""
)

# ---------------------------------
# MAIN LOGIC
# ---------------------------------

result_rows = []

for i in range(len(df)):

    combined_name = df.loc[i, "Combined"]
    short_name = df.loc[i, "ShortName"]
    last_name = df.loc[i, "Last Name"]

    # Skip blank combined
    if combined_name == "":
        continue

    # ---------------------------------
    # MATCH 1:
    # Combined exists in First Name
    # + same Last Name
    # ---------------------------------

    match1 = df[
        (df["First Name"] == combined_name) &
        (df["Last Name"] == last_name)
    ]

    if not match1.empty:

        # ---------------------------------
        # MATCH 2:
        # ShortName exists in First Name
        # + same Last Name
        # + Middle Name should NOT be blank
        # ---------------------------------

        match2 = df[
            (df["First Name"] == short_name) &
            (df["Last Name"] == last_name) &
            (df["Middle Name"] != "")
        ]

        if not match2.empty:

            # Add matched rows
            result_rows.append(match1.iloc[0])
            result_rows.append(match2.iloc[0])

# ---------------------------------
# FINAL OUTPUT
# ---------------------------------

result_df = pd.DataFrame(result_rows).drop_duplicates()

# Save Excel
result_df.to_excel("Cheks.xlsx", index=False)

print("Done! Output saved as Cheks.xlsx")