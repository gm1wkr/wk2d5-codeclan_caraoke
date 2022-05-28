import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Seventies")
        self.song_1 = Song("Time Warp", "Richard O'Brian")
        self.song_2 = Song("One Vision", "Queen")
        self.song_3 = Song("Schools Out", "Alice Cooper")
        self.startrek_song = Song("Star Trekking (Across The Universe)", "The Firm")
        self.guest_1 = Guest("Will Reiker", 10, self.song_1)
        self.guest_2 = Guest("Arthur Dent", 10, self.song_2)
        self.guest_3 = Guest("Slarty Bartfast", 10, self.song_3)

    def test_room_has_name(self):
        self.assertEqual("Seventies", self.room_1.name)

    def test_room_has_entry_fee(self):
        self.assertEqual(2.5, self.room_1.room_entry_fee)

    def test_room_has_till(self):
        self.assertEqual(100, self.room_1.till)

    def test_does_room_have_capacity(self):
        self.assertEqual(True, self.room_1.room_has_capacity())
        
    def test_does_room_have_capacity__False(self):
        self.room_full = Room("ChokaBlock")
        self.room_full.max_allowed_guest = 0
        self.assertEqual(True, self.room_1.room_has_capacity())


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

    def test_room_is_guest_in_room__True(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.assertEqual(True, self.room_1.is_guest_in_room(self.guest_1))
    
    def test_room_is_guest_in_room__False(self):
        self.room_1.add_guest_to_guest_list(self.guest_1)
        self.guest_abscent = Guest("Ensign Insignificant", 100, self.song_1)
        self.assertEqual(False, self.room_1.is_guest_in_room(self.guest_abscent))

    def test_room_is_song_in_playlist__Not_found(self):
        self.assertEqual(False, self.room_1.is_song_in_playlist(self.song_1))
    
    def test_room_add_song_to_playlist(self):
        self.song_to_add = Song("Lucille", "BB King")
        self.room_no_play_list = Room("Empty Playlist")
        self.room_no_play_list.add_song_to_playlist(self.song_to_add)
        self.assertEqual(1, self.room_no_play_list.number_of_songs_in_playlist())


    def test_room_has_guest_favourite_song__False(self):
        self.captains_mess = Room("Captains Mess")
        self.janeways_favourite_song = Song("Urban Spaceman", "Bonzo Dog Do Dah Band")
        self.guest_janeway = Guest("Captain Catherine Janeway", 10, self.janeways_favourite_song)
        # self.captains_mess.add_song_to_playlist(self.janeways_favourite_song)
        self.assertEqual(False, self.captains_mess.room_has_guest_favourite_song(self.guest_janeway))
    
    def test_room_has_guest_favourite_song__True(self):
        self.captains_mess = Room("Captains Mess")
        self.janeways_favourite_song = Song("Urban Spaceman", "Bonzo Dog Do Dah Band")
        self.guest_janeway = Guest("Captain Catherine Janeway", 10, self.janeways_favourite_song)
        self.captains_mess.add_song_to_playlist(self.janeways_favourite_song)
        self.assertEqual('Gie’in It Laldy', self.captains_mess.room_has_guest_favourite_song(self.guest_janeway))

    def test_room_check_in_guest__ok(self):
        self.ten_forward = Room("Ten Forward")
        self.startrek_song = Song("Star Trekking (Across The Universe)", "The Firm")
        self.guest_warf = Guest("Lt Warf", 10, self.startrek_song)
        self.ten_forward.check_in_guest(self.guest_warf)
        self.ten_forward.add_song_to_playlist(self.guest_warf.favourite_song)


        self.assertEqual(True, self.ten_forward.room_has_capacity())
        self.assertEqual(True, self.ten_forward.guest_has_entry_fee(self.guest_warf))
        self.assertEqual(7.5, self.guest_warf.wallet)
        self.assertEqual(102.5, self.ten_forward.till)
        self.assertEqual(True, self.ten_forward.is_guest_in_room(self.guest_warf))


    def test_room_number_of_guests_checked_in__add(self):
        self.ten_forward = Room("Ten Forward")
        self.ten_forward.check_in_guest(self.guest_1)
        self.ten_forward.check_in_guest(self.guest_2)
        self.ten_forward.check_in_guest(self.guest_3)
        self.assertEqual(3, self.ten_forward.number_guest_checked_in())

    def test_room_get_guest_list(self):
        self.ten_forward = Room("Ten Forward")
        self.ten_forward.check_in_guest(self.guest_1)
        self.ten_forward.check_in_guest(self.guest_2)
        self.ten_forward.check_in_guest(self.guest_3)
        expected_list = ['Will Reiker', 'Arthur Dent', 'Slarty Bartfast']
        self.assertEqual(expected_list, self.ten_forward.get_list_of_guest_names())

    # def test_room_check_out(self):
    #     self.ten_forward = Room("Ten Forward")
    #     self.startrek_song = Song("Star Trekking (Across The Universe)", "The Firm")
    #     self.guest_warf = Guest("Lt Warf", 10, self.startrek_song)
    #     self.ten_forward.check_in_guest(self.guest_1)
    #     self.ten_forward.check_in_guest(self.guest_2)
    #     self.ten_forward.check_in_guest(self.guest_3)
    #     self.ten_forward.check_in_guest(self.guest_warf)
        
    #     self.ten_forward.checkout_guest(self.guest_warf)
    #     self.assertEqual(3, self.ten_forward.number_guest_checked_in())


