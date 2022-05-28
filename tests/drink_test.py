import unittest

from src.drink import Drink
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.room = Room("Oldies")
        self.guest_fav_song = Song("Man of Constant Sorrow", "Soggy Bottom Boys")
        self.guest = Guest("Basil Fawlty", 100, self.guest_fav_song)

        self.drink_whiskey = Drink("Whiskey")

    def test_drink_has_name(self):
        self.assertEqual("Whiskey", self.drink_whiskey.name)

    def test_drink_has_stock_level(self):
        self.assertEqual(10, self.drink_whiskey.stock_level)