from abc import ABC, abstractmethod

# ABSTRACTION
class MusicPlayer(ABC):

    def __init__(self, volume):
        self.__volume = volume       # DATA HIDING

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self.__volume = volume

    @abstractmethod
    def play(self):
        pass


# DYNAMIC BINDING
class Spotify(MusicPlayer):

    def play(self):
        print("Playing song on Spotify")


class YouTubeMusic(MusicPlayer):

    def play(self):
        print("Playing song on YouTube Music")


# Objects
player = Spotify(50)
player.play()
print("Volume:", player.get_volume())

player = YouTubeMusic(70)
player.play()
print("Volume:", player.get_volume())
