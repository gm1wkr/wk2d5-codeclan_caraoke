class BarTab:
    def __init__(self, guest):
        self.guest = guest
        self.running_total = 4

    def add_to_tab(self, amount):
        self.running_total += amount

    def settle_tab(self, guest):
        self.running_total = 0.0