import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../laptop.csv', encoding='windows-1251')

filtered = df[
    (df['TypeName'] == 'Gaming') &
    (df['Gpu'] == 'Nvidia GeForce GTX 1060') &
    (df['Inches'] != 17.3) &
    (df['Price_euros'] <= 1800)
    ]
filtered = filtered.sort_values(['Price_euros', 'laptop_ID'])
print(f"Количество: {len(filtered)}")
print()
print(filtered[['laptop_ID', 'Company', 'Product', 'Inches', 'Price_euros']].head().to_string(index=False))
