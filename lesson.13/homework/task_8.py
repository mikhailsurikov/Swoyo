import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('../laptop.csv', encoding='windows-1251')


def get_display_type(screen_resolution: str) -> str:
    has_ips = 'IPS Panel' in screen_resolution
    has_touch = 'Touchscreen' in screen_resolution

    if has_ips and has_touch:
        return 'IPS Touch'
    if has_touch:
        return 'Touch'
    if has_ips:
        return 'IPS'
    return 'Обычный'


df['Display_type'] = df['ScreenResolution'].apply(get_display_type)


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
    (df['Display_type'] == 'IPS') &
    (df['Storage_type'] == 'SSD + HDD') &
    (df['OpSys'] == 'Windows 10') &
    (df['Price_euros'] >= 1000) &
    (df['Price_euros'] <= 1600)
    ]
filtered = filtered[[
    'laptop_ID', 'Company', 'Product', 'TypeName',
    'Memory', 'Price_euros', 'Display_type', 'Storage_type'
]]
filtered = filtered.sort_values(
    ['Company', 'Price_euros', 'laptop_ID'],
    ascending=[True, False, True],
)
filtered = filtered.reset_index(drop=True)
print(f"Количество: {len(filtered)}")
print('Первые 5:')
print(filtered.head().to_string(index=False))
filtered.to_csv('final_catalog.csv', index=False, encoding='utf-8')
