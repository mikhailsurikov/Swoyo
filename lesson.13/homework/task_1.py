import pandas as pd

df = pd.read_csv('../laptop.csv', encoding='windows-1251')
chrome = df[df['OpSys'] == 'Chrome OS']
print(f"Количество: {len(chrome)}")
print(chrome[['Company', 'Product', 'TypeName', 'OpSys', 'Price_euros']].head())
