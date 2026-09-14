# Задание 8 ⭐. Анализ журнала событий
# Дан список:
# logs = [
#     "2026-09-10 10:15:00 | 200",
#     "2026-09-10 10:18:30 | 500",
#     "2026-09-10 10:20:00 | 404",
#     "2026-09-10 10:32:10 | 200"
# ]
# Используя `re` и `datetime`:
# 1. извлеките дату и время каждой записи;
# 2. извлеките код статуса;
# 3. посчитайте количество ошибок — статус `400` и выше;
# 4. определите время между первой и последней записью списка.

import re
from datetime import datetime as dt

logs = [
    "2026-09-10 10:15:00 | 200",
    "2026-09-10 10:18:30 | 500",
    "2026-09-10 10:20:00 | 404",
    "2026-09-10 10:32:10 | 200"
]
pattern = re.compile(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \| (\d{3})")
records = []
for line in logs:
    match = pattern.search(line)
    if match:
        dt_str, status_str = match.groups()
        dt = dt.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        status = int(status_str)
        records.append((dt, status))

errors = sum(1 for _, status in records if status >= 400)
delta = records[-1][0] - records[0][0]

print(f'Ошибок: {errors}')
print(f'Период: {delta}')
