# Даны значения:
# [120, 180, 240, 300, 360]
# Создайте из них NumPy-массив с типом:
# np.int16
# Выведите:
# * массив;
# * количество измерений;
# * форму;
# * количество элементов;
# * тип данных;
# * размер одного элемента в байтах;
# * общий объём массива в байтах.

import numpy as np

np_array = np.array([120, 180, 240, 300, 360], dtype=np.int16)
print(np_array)
print(f"Измерений: {np_array.ndim}")
print(f"Форма: {np_array.shape}")
print(f"Элементов: {np_array.size}")
print(f"Тип: {np_array.dtype}")
print(f"Размер элемента: {np_array.itemsize}")
print(f"Размер массива: {np_array.nbytes}")
