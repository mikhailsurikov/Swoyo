# Задание 3. Трекер активности
# Создайте класс:
# FitnessTracker
# При создании объекта количество шагов должно быть равно `0`.
# Добавьте методы:
# add_steps(count) добавляет указанное количество шагов.(Нельзя добавить отрицательное количество шагов.)
# get_steps()  возвращает текущее количество шагов.
# get_distance() возвращает примерное пройденное расстояние в километрах.(Считайте, что один шаг равен: 0.0008 км)
# reset() сбрасывает количество шагов до 0

class FitnessTracker:
    def __init__(self):
        self.steps = 0

    def add_steps(self, step):
        if step < 0:
            print('Некорректное количество шагов')
            return
        else:
            self.steps += step

    def get_steps(self):
        return self.steps

    def get_distance(self):
        step_ratio = 0.0008
        return self.steps * step_ratio

    def reset(self):
        self.steps = 0


tracker = FitnessTracker()

tracker.add_steps(3000)
tracker.add_steps(2000)
tracker.add_steps(-2000)

print("Шагов:", tracker.get_steps())
print("Расстояние:", tracker.get_distance(), "км")

tracker.reset()

print("Шагов:", tracker.get_steps())
