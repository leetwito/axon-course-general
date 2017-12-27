#
# Provided a text file with information about artists and songs:
#
# Joy Division - Love Will Tear Us Apart
# Joy Division - New Dawn Fades
# Pixies - Where Is My Mind
# Pixies - Hey
# Genesis - Mama
#
# Write the required classes so the following code works:
#
# music = MusicFile('/Users/ynonperek/music.txt')
# print(music.artist('Joy Division').songs)


class MusicFile(object):
    def __init__(self, path):
        _file = open(path, 'r')
        self._list = _file.read().splitlines()


    def artist(self, name):
        artist = Artist(name)
        for line in self._list:
            end_index = line.find(' - ')
            singer_name = line[:end_index]
            song_name = line[end_index+3:]
            # print(singer_name)
            # print(song_name)
            if singer_name == name:
                artist.addSong(song_name)
        return artist


class Artist(object):
    def __init__(self, name):
        self._song_name_index = len(name) - 1 + 4
        self.songs = []

    def addSong(self, song_name):
        self.songs.append(song_name)


def main():
    music = MusicFile('/home/student-6/PycharmProjects/23.11/music.txt')
    print(music.artist('Joy Division').songs)

if __name__== "__main__":
    main()
