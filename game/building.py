import pygame

class Building:
    def __init__(self, x, y, building_type):
        self.x = x
        self.y = y
        self.building_type = building_type  # "wall", "chest", "campfire", "bed"
        self.width = 40
        self.height = 40
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.health = 100
    
    def draw(self, screen):
        if self.building_type == "wall":
            pygame.draw.rect(screen, (101, 67, 33), (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, (139, 90, 43), (self.x, self.y, self.width, self.height), 3)
        
        elif self.building_type == "chest":
            pygame.draw.rect(screen, (218, 165, 32), (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, (184, 134, 11), (self.x, self.y, self.width, self.height), 2)
        
        elif self.building_type == "campfire":
            pygame.draw.rect(screen, (50, 50, 50), (self.x, self.y, self.width, self.height))
            pygame.draw.circle(screen, (255, 100, 0), (int(self.x + 20), int(self.y + 20)), 15)
        
        elif self.building_type == "bed":
            pygame.draw.rect(screen, (200, 100, 100), (self.x, self.y, self.width, self.height))
            pygame.draw.rect(screen, (150, 50, 50), (self.x, self.y, self.width, self.height), 2)
    
    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0


class BuildingSystem:
    def __init__(self):
        self.buildings = []
        self.material_costs = {
            "wall": {"wood": 5, "stone": 2},
            "chest": {"wood": 10},
            "campfire": {"wood": 3, "stone": 5},
            "bed": {"wood": 8}
        }
    
    def can_build(self, building_type, inventory):
        """Check if player has enough materials"""
        costs = self.material_costs.get(building_type, {})
        for material, amount in costs.items():
            if inventory.count(material) < amount:
                return False
        return True
    
    def build(self, building_type, x, y, inventory):
        """Build a structure and consume materials"""
        if not self.can_build(building_type, inventory):
            print(f"Not enough materials to build {building_type}!")
            return False
        
        # Consume materials
        costs = self.material_costs.get(building_type, {})
        for material, amount in costs.items():
            for _ in range(amount):
                inventory.remove(material)
        
        # Create building
        building = Building(x, y, building_type)
        self.buildings.append(building)
        print(f"Built {building_type} at ({x}, {y})!")
        return True
    
    def get_building_info(self):
        """Get building costs info for UI"""
        return {
            "wall": "Wall - Wood: 5, Stone: 2",
            "chest": "Chest - Wood: 10",
            "campfire": "Campfire - Wood: 3, Stone: 5",
            "bed": "Bed - Wood: 8"
        }
    
    def draw(self, screen):
        for building in self.buildings:
            building.draw(screen)
    
    def update(self):
        # Remove destroyed buildings
        self.buildings = [b for b in self.buildings if b.health > 0]
