# Задание 2. Резерв товара
# Средствами NumPy создайте два массива по `6` элементов:
# * первый состоит из нулей;
# * второй состоит из единиц.
# Тип данных:
# np.int16
# Получите из второго массива:
# [5 5 5 5 5 5]
# После этого сложите его с массивом нулей.
# Массивы нельзя создавать ручным перечислением элементов.
import numpy as np

zerros_array = np.zeros(6, dtype=np.int16)
reserv_array = np.ones(6, dtype=np.int16)
print(f'Нули: {zerros_array}')
reserv_array += 4
print(f'Резерв: {reserv_array}')
print(f'Результат: {reserv_array + zerros_array}')
