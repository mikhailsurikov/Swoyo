# Задание 2. Плейлист
# Создайте класс:
# Playlist
# У плейлиста должно быть название и список песен.
# При создании объекта список песен пустой.
# Добавьте методы:
# add_song(song) добавляет песню в плейлист.
# show_songs() выводит все песни.
# songs_count() возвращает количество песен.

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song_name):
        self.songs.append(song_name)

    def show_songs(self):
        print(*self.songs, sep='\n')

    def songs_count(self):
        return len(self.songs)


playlist = Playlist("Для работы")

playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

playlist.show_songs()
print("Количество песен:", playlist.songs_count())
