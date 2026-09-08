# Задание 2. Очередь задач
# Создайте класс:
# TaskQueue
# Внутри должен храниться список задач.
# Добавьте методы:
# add_task(task)
# complete_task()
# __len__()
# `add_task()` добавляет задачу в конец очереди.
# `complete_task()` удаляет и возвращает первую задачу.
# Если очередь пуста, `complete_task()` должен вернуть `None`.
# `len(queue)` должен возвращать количество оставшихся задач.

class TaskQueue:
    """Класс Очередь задач.
    Содержит список задач
    """

    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)

    def complete_task(self):
        if self.task_list:
            return self.task_list.pop(0)

    def __len__(self):
        return len(self.task_list)


queue = TaskQueue()

queue.add_task("Ответить на письмо")
queue.add_task("Проверить отчёт")
queue.add_task("Позвонить клиенту")

print(queue.complete_task())
print(len(queue))
