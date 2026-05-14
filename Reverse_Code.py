import pandas as pd

# =========================
# =========================
input_file = "Raw.xlsx"   # apni file ka naam
df = pd.read_excel(input_file)

# =========================
# 2. First Name + Last Name
# =========================
df["Full Name"] = (
    df["First Name"].astype(str).str.strip() + " " +
    df["Last Name"].astype(str).str.strip()
)

df["Reverse Name"] = (
    df["Last Name"].astype(str).str.strip() + " " +
    df["First Name"].astype(str).str.strip()
)

# =========================
# 3. Matching Logic
# =========================
full_name_set = set(df["Full Name"])

matched_rows = []

for _, row in df.iterrows():

    full_name = row["Full Name"]
    reverse_name = row["Reverse Name"]

    # check karo reverse name full name column me exist karta hai ya nahi
    if reverse_name in full_name_set:

        matched_rows.append({
            "Name 1": full_name,
            "Name 2": reverse_name
        })

# =========================
# 4. DataFrame Banaao
# =========================
result_df = pd.DataFrame(matched_rows)

# =========================
# 5. Duplicate Reverse Pair Remove
# =========================
def create_key(row):

    a = row["Name 1"]
    b = row["Name 2"]

    # alphabetically arrange
    if a < b:
        return a + "|" + b
    else:
        return b + "|" + a

result_df["Key"] = result_df.apply(create_key, axis=1)

# duplicates remove
result_df = result_df.drop_duplicates(subset=["Key"])

# optional: key column remove
result_df = result_df.drop(columns=["Key"])

# =========================
# 6. Final Export
# =========================
output_file = "Reverse Name.xlsx"

result_df.to_excel(output_file, index=False)

print("Done ✅ Final file saved as:", output_file)
