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

    def test_tab_has_guest_name(self):
        self.assertEqual("Basil Fawlty", self.bar_tab.guest.name)


    def test_tab_has_running_total(self):
        self.assertEqual(4, self.bar_tab.running_total)


    def test_add_to_tab(self):
        self.bar_tab.add_to_tab(2.5)
        self.assertEqual(6.5, self.bar_tab.running_total)

    def test_settle_tab(self) :
        self.bar_tab.settle_tab(self.guest)
        self.assertEqual(0.0, self.bar_tab.running_total)