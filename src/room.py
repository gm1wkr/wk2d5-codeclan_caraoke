class Room:
    def __init__(self, name, room_entry_fee=5, till=100, max_allowed_guests=20) :
        self.name = name
        self.room_entry_fee =room_entry_fee
        self.till = till
        self.max_allowed_guest = max_allowed_guests

        