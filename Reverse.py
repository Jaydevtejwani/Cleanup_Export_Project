import pandas as pd

df = pd.DataFrame({
    'name': [
        'Jay Dev Tejwani',
        'Tejwani Jay Dev',
        'John Doe',
        'Doe John',
        'Amit Kumar'
    ]
})

# normalize key (words sort karke same ban jaye dono direction me)
df['key'] = df['name'].apply(lambda x: ' '.join(sorted(x.lower().split())))

# group by key
result = df.groupby('key')['name'].apply(list).reset_index()

# sirf pairs filter karo (jisme reverse match mila ho)
result = result[result['name'].apply(lambda x: len(x) > 1)]

print(result)
