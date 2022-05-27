import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Time Warp", "Richard O'Brian")
        self.guest_1 = Guest("Will Reiker", 10, self.song_1)

    def test_guest_has_name(self):
        self.assertEqual("Will Reiker", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(10, self.guest_1.wallet)

    def test_guest_reduce_wallet(self):
        self.guest_1.reduce_wallet(1)
        self.assertEqual(9, self.guest_1.wallet)
    
    def test_guest_has_favourite_song(self):
        self.assertEqual("Time Warp", self.guest_1.favourite_song)