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