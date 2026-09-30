import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../laptop.csv', encoding='windows-1251')

filtered = df[
    (df['Ram'].isin(['8GB', '16GB'])) &
    (df['OpSys'] == 'Windows 10') &
    (df['Price_euros'] <= 500)
]

print(f"Количество вариантов: {len(filtered)}")
print(filtered[['Company', 'Product', 'Ram', 'OpSys', 'Price_euros']].head())
