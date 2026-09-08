from abc import ABC, abstractmethod


# Задание 7. Абстрактный медиаплеер
# Создайте абстрактный класс:
# MediaFile
# Используйте:
# from abc import ABC, abstractmethod
# При создании объекта передавайте название файла.
# Добавьте абстрактный метод:
# play()
# Создайте дочерние классы:
# AudioFile
# VideoFile
# Podcast
# Каждый класс должен реализовать `play()` по-своему.

class MediaFile(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def play(self):
        pass


class AudioFile(MediaFile):
    def play(self):
        return f'Воспроизводим аудио {self.name}'


class VideoFile(MediaFile):
    def play(self):
        return f'Воспроизводим видео {self.name}'


class Podcast(MediaFile):
    def play(self):
        return f'Запускаем подкаст {self.name}'


files = [
    AudioFile("music.mp3"),
    VideoFile("lesson.mp4"),
    Podcast("python.mp3"),
]

for file in files:
    print(file.play())
