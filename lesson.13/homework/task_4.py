import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

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

counts = df['Display_type'].value_counts()

for label in ['IPS Touch', 'Touch', 'IPS', 'Обычный']:
    print(f"{label}: {counts.get(label, 0)}")
