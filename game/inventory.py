class Inventory:
    def __init__(self, max_size=20):
        self.items = []
        self.max_size = max_size
    
    def add(self, item, quantity=1):
        for i in range(quantity):
            if len(self.items) < self.max_size:
                self.items.append(item)
            else:
                print("Inventory full!")
                return False
        return True
    
    def add_items(self, items):
        for item in items:
            self.add(item)
    
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def has(self, item):
        return item in self.items
    
    def count(self, item):
        return self.items.count(item)
    
    def get_all_items(self):
        return self.items
    
    def get_item_counts(self):
        # Return a dict with item names and quantities
        counts = {}
        for item in self.items:
            counts[item] = counts.get(item, 0) + 1
        return counts
    
    def clear(self):
        self.items = []
    
    def is_full(self):
        return len(self.items) >= self.max_size
    
    def get_space_left(self):
        return self.max_size - len(self.items)
