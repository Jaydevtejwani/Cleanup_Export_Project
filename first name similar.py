import pandas as pd
from rapidfuzz import fuzz

df = pd.read_excel("Data.xlsx")  


matches = []

for first_name, group in df.groupby("First Name"):

    names = group["Last Name"].tolist()

    for i in range(len(names)):
        for j in range(i + 1, len(names)):

            score = fuzz.ratio(names[i], names[j])

            if score >= 80 and score <= 95:
                matches.append({
                    "first Name": first_name,
                    "last_name_1": names[i],
                    "last_name_2": names[j],
                    "similarity_percent": score
                })

result = pd.DataFrame(matches)

result.to_excel("matched_results.xlsx", index=False)

print(result)