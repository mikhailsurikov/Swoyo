# Задание 5. Громкость аудиоплеера
# Создайте класс:
# AudioPlayer
# Уровень громкости должен храниться в приватном атрибуте:
# __volume
# Добавьте методы:
# get_volume()
# set_volume(volume)
# volume_up()
# volume_down()
# Громкость может принимать значения только от `0` до `100`.
# `volume_up()` увеличивает громкость на `10`.
# `volume_down()` уменьшает громкость на `10`.
# Значение не должно выходить за допустимые границы.

class AudioPlayer:
    def __init__(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.__volume = volume
        else:
            print('Некорректная громкость')

    def volume_up(self):
        if self.__volume + 10 > 100:
            print('Достигнута максимальная громкость')
        else:
            self.__volume += 10

    def volume_down(self):
        if self.__volume - 10 < 0:
            print('Достигнута минимальная громкость')
        else:
            self.__volume -= 10


player = AudioPlayer(50)

player.volume_up()
print(player.get_volume())
player.volume_up()
print(player.get_volume())
player.volume_down()
print(player.get_volume())
player.set_volume(150)
print(player.get_volume())
player.set_volume(10)
print(player.get_volume())
