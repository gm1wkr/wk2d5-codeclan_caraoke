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

    def test_room_has_entry_fee(self):
        self.assertEqual(5, self.room_1.room_entry_fee)

    def test_room_has_custom_entry_fee(self):
        self.room_custom_entry = Room("Expensive", 20)
        self.assertEqual(20, self.room_custom_entry.room_entry_fee)

    def test_room_has_till(self):
        self.assertEqual(100, self.room_1.till)
    