import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Time Warp", "Richard O'Brian")
        self.song_2 = Song("We are the Champions", "Queen")
        self.song_3 = Song("Canyons of My Mind", "Bonzo Dog Doo Dah Band")


    def test_song_has_name(self):
        self.assertEqual("Time Warp", self.song_1.name)


    def test_song_has_artist(self):
        self.assertEqual("Richard O'Brian", self.song_1.artist)


    def test_song_has_playcount(self):
        self.song_2.play_count = 10
        self.assertEqual(10, self.song_2.play_count)


    def test_increase_song_play_count(self):
        self.song_3.increase_play_count(2)
        self.assertEqual(2, self.song_3.play_count)


    def test_get_play_count(self):
        self.song_2.increase_play_count(1)
        self.assertEqual(1, self.song_2.get_play_count())
