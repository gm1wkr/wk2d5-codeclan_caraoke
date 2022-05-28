class Room:
    def __init__(self, name) :
        self.name = name
        self.room_entry_fee = 2.5
        self.till = 100
        self.max_allowed_guest = 30
        self.room_guest_list = []
        self.room_playlist = []


    def room_has_capacity(self):
        return len(self.room_guest_list) < self.max_allowed_guest

    def guest_has_entry_fee(self, guest):
        return guest.wallet > self.room_entry_fee

    def take_entry_fee_from_guest(self, guest):
        if self.guest_has_entry_fee:
            guest.wallet -= self.room_entry_fee
            self.add_to_till(self.room_entry_fee)

    def add_to_till(self, amount):
        self.till += amount

    def is_guest_in_room(self, guest):
        return guest in self.room_guest_list

    def add_guest_to_guest_list(self, guest):
        if not self.is_guest_in_room(guest):
            self.room_guest_list.append(guest)

    def is_song_in_playlist(self, song_to_find):
        for song in self.room_playlist:
            if song.name == song_to_find.name:
                return True
        return False

    def number_of_songs_in_playlist(self):
        return len(self.room_playlist)

    def add_song_to_playlist(self, song_to_add):
        self.room_playlist.append(song_to_add)

    def room_has_guest_favourite_song(self, guest):
        for song in self.room_playlist:
            if song.name == guest.favourite_song:
                return guest.cheer_loudly()
        return False


    def check_in_guest(self, guest):
        if self.room_has_capacity():
            
            self.take_entry_fee_from_guest(guest)
            # self.add_to_till(self.room_entry_fee)
            self.add_guest_to_guest_list(guest)
            # print statement so Guest is heard cheering loudly!
            if self.room_has_guest_favourite_song(guest):
                print(guest.cheer_loudly())



