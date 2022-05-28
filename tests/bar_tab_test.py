import unittest

from src.bar_tab import BarTab
from src.drink import Drink
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestBarTab(unittest.TestCase):
    def setUp(self):
        self.room = Room("Oldies")
        self.guest_fav_song = Song("Man of Constant Sorrow", "Soggy Bottom Boys")
        self.guest = Guest("Basil Fawlty", 100, self.guest_fav_song)
        self.drink_1 = Drink("Whiskey", 10)
        self.bar_tab = BarTab(self.guest)