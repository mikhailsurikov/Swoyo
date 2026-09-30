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

filtered = df[
    (df['Display_type'] == 'IPS Touch') &
    (df['TypeName'] == '2 in 1 Convertible') &
    (df['Price_euros'] <= 1500)
    ]

filtered = filtered.sort_values(['Price_euros', 'laptop_ID'])

print(f"Количество: {len(filtered)}")
print()
print(filtered[['laptop_ID', 'Company', 'Product', 'Inches', 'Price_euros']].head().to_string(index=False))
