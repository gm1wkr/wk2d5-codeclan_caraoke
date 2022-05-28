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

        self.drink_whiskey = Drink("Whiskey", 2.5)
        self.drink_coke = Drink("Coke", 1.0)
        self.drink_mead = Drink("Mead", 2.0)
        self.drink_oj = Drink("OJ", 2.5)

    def test_drink_has_name(self):
        self.assertEqual("Whiskey", self.drink_whiskey.name)

    def test_drink_has_stock_level(self):
        self.assertEqual(10, self.drink_whiskey.stock_level)

    def test_get_stock_level(self):
        self.assertEqual(10, self.drink_whiskey.stock_level)

    def test_reduce_stock_level_by(self):
        self.drink_whiskey.reduce_stock_level_by(2)
        self.assertEqual(8, self.drink_whiskey.stock_level)

    def test_get_price_of_drink(self):
        self.assertEqual(2.0, self.drink_mead.get_price())