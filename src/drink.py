class Drink:
    def __init__(self, name):
        self.name = name
        self.stock_level = 10

    def get_stock_level(self):
        return self.stock_level

    
    def reduce_stock_level_by(self, number_sold):
        self.stock_level -= number_sold