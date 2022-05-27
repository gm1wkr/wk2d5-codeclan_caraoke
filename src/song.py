class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.play_count = 0

    def increase_play_count(self, increase_by):
        self.play_count += increase_by