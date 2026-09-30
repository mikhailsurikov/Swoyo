import pandas as pd

df = pd.read_csv('../laptop.csv', encoding='windows-1251')
min_inches = df['Inches'].min()
smallest = df[df['Inches'] == min_inches]
print(f"Минимальная диагональ: {min_inches}")
print(f"Количество моделей: {len(smallest)}")
print()
print(smallest[['Company', 'Product', 'TypeName', 'Inches', 'Price_euros']].to_string(index=False))
