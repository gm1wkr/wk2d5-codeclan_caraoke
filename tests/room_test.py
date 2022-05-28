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
        self.assertEqual(2.5, self.room_1.room_entry_fee)

    def test_room_has_till(self):
        self.assertEqual(100, self.room_1.till)

    def test_does_room_have_capacity(self):
        self.assertEqual(True, self.room_1.room_has_capacity())
        
    # def test_does_room_have_capacity__False(self):
    #     self.room_full = Room("ChokaBlock")
    #     self.room_full.max_allowed_guest = 0
    #     self.assertEqual(True, self.room_1.room_has_capacity())


    def test_guest_has_entry_fee__true(self):
        self.assertEqual(True, self.room_1.guest_has_entry_fee(self.guest_1))

    def test_guest_has_entry_fee__False(self):
        self.guest_no_money = Guest("Tom Paris", 2, self.song_1)
        self.assertEqual(False, self.room_1.guest_has_entry_fee(self.guest_no_money))

    def test_take_entry_fee_from_guest(self):
        self.room_1.take_entry_fee_from_guest(self.guest_1)
        self.assertEqual(7.5, self.guest_1.wallet)

    def test_room_add_to_till(self):
        self.room_1.add_to_till(self.room_1.room_entry_fee)
        self.assertEqual(102.5, self.room_1.till)

    def test_room_add_guest_to_guest_list(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.assertEqual("Will Reiker", self.room_1.room_guest_list[0].name)

    def test_room_check_in_guest__ok(self):
        # check does room have capacity for another
        # take entry fee from guest
        # put entry fee in room till
        # add guest to room guest list
        # is guests favourite song in room playlist.
        pass




    # def test_room_has_till__custom_float(self):
    #     self.room_with_big_till = Room("Loads in Till")
    #     self.assertEqual(100, self.room_1.till)
    # # def test_room_has_custom_entry_fee(self):
    # #     self.room_custom_entry = Room("Expensive")
    # #     self.assertEqual(20, self.room_custom_entry.room_entry_fee)