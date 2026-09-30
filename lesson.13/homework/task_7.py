import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../laptop.csv', encoding='windows-1251')


def get_storage_type(memory: str) -> str:
    has_ssd = 'SSD' in memory
    has_hdd = 'HDD' in memory

    if has_ssd and has_hdd:
        return 'SSD + HDD'
    if has_ssd:
        return 'SSD'
    if has_hdd:
        return 'HDD'
    return 'Другое'


df['Storage_type'] = df['Memory'].apply(get_storage_type)
filtered = df[
    (df['Storage_type'] == 'SSD + HDD') &
    (df['TypeName'] == 'Gaming') &
    (df['OpSys'] == 'Windows 10') &
    (df['Price_euros'] <= 1800)
    ]
filtered = filtered.sort_values(['Price_euros', 'laptop_ID'])
print(f"Количество: {len(filtered)}")
print()
print(filtered[['laptop_ID', 'Company', 'Product', 'Memory', 'Price_euros']].head().to_string(index=False))
