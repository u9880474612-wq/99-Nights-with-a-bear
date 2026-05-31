class Inventory:
    def __init__(self):
        self.raw_meat = 0
        self.cooked_meat = 0
        self.vegetables = 0
        self.fish = 0
        self.wood = 0
        self.gold = 0
        self.items = []
    
    def add_item(self, item_type, amount=1):
        if item_type == 'raw_meat':
            self.raw_meat += amount
        elif item_type == 'cooked_meat':
            self.cooked_meat += amount
        elif item_type == 'vegetables':
            self.vegetables += amount
        elif item_type == 'fish':
            self.fish += amount
        elif item_type == 'wood':
            self.wood += amount
        elif item_type == 'gold':
            self.gold += amount
    
    def remove_item(self, item_type, amount=1):
        if item_type == 'raw_meat':
            self.raw_meat -= amount
        elif item_type == 'cooked_meat':
            self.cooked_meat -= amount
        elif item_type == 'vegetables':
            self.vegetables -= amount
        elif item_type == 'fish':
            self.fish -= amount
        elif item_type == 'wood':
            self.wood -= amount
        elif item_type == 'gold':
            self.gold -= amount
    
    def get_total_items(self):
        return (self.raw_meat + self.cooked_meat + self.vegetables + 
                self.fish + self.wood + self.gold)
