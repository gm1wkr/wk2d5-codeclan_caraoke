import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Time Warp", "Richard O'Brian")
        self.guest_1 = Guest("Will Reiker", 10, self.song_1)

    def test_guest_has_name(self):
        self.assertEqual("Will Reiker", self.guest_1.name)