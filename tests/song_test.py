import unittest


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