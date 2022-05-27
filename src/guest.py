class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song.name


    def reduce_wallet(self, reduce_by):
        if self.wallet >= reduce_by:
            self.wallet -= reduce_by