import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Seventies")
        self.song_1 = Song("Time Warp", "Richard O'Brian")
        self.guest_1 = Guest("Will Reiker", 10, self.song_1)

    def test_room_has_name(self):
        self.assertEqual("Seventies", self.room_1.name)