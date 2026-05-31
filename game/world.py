import pygame
import random

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        # Cave location
        self.cave_x = width - 200
        self.cave_y = height - 200
        self.cave_width = 150
        self.cave_height = 150
        
        # Fence around forest
        self.fence_center_x = width // 2
        self.fence_center_y = height // 2
        self.fence_radius = 300
        
        # World objects
        self.trees = self.generate_trees()
        self.chests = self.generate_chests()
        self.water = (100, 50, 200, 150)  # x, y, width, height
        self.animals = self.generate_animals()
        self.bed_x = self.cave_x + 30
        self.bed_y = self.cave_y + 30
    
    def generate_trees(self):
        trees = []
        for _ in range(15):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            trees.append((x, y, 30, 30))  # x, y, width, height
        return trees
    
    def generate_chests(self):
        chests = []
        for _ in range(5):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            chests.append({'x': x, 'y': y, 'opened': False, 'items': random.randint(10, 50)})
        return chests
    
    def generate_animals(self):
        animals = []
        for _ in range(8):
            x = random.randint(50, self.width - 50)
            y = random.randint(50, self.height - 50)
            animal_type = random.choice(['deer', 'wolf'])
            animals.append({'x': x, 'y': y, 'type': animal_type, 'health': 50})
        return animals
    
    def update(self, time_system):
        # Update animal positions
        for animal in self.animals:
            animal['x'] += random.uniform(-2, 2)
            animal['y'] += random.uniform(-2, 2)
            # Keep in bounds
            animal['x'] = max(0, min(self.width - 20, animal['x']))
            animal['y'] = max(0, min(self.height - 20, animal['y']))
    
    def draw(self, screen):
        # Draw grass
        screen.fill((34, 139, 34))
        
        # Draw trees
        for x, y, w, h in self.trees:
            pygame.draw.rect(screen, (0, 100, 0), (x, y, w, h))
        
        # Draw water
        pygame.draw.rect(screen, (0, 100, 200), self.water)
        
        # Draw cave
        pygame.draw.rect(screen, (50, 50, 50), (self.cave_x, self.cave_y, self.cave_width, self.cave_height))
        pygame.draw.rect(screen, (100, 100, 100), (self.cave_x + 10, self.cave_y + 10, 30, 30))  # Cave door
        
        # Draw bed in cave
        pygame.draw.rect(screen, (139, 69, 19), (self.bed_x, self.bed_y, 50, 40))
        
        # Draw chests
        for chest in self.chests:
            color = (184, 134, 11) if not chest['opened'] else (100, 100, 100)
            pygame.draw.rect(screen, color, (chest['x'], chest['y'], 30, 20))
        
        # Draw fence (circle outline)
        pygame.draw.circle(screen, (139, 69, 19), (self.fence_center_x, self.fence_center_y), self.fence_radius, 3)
    
    def draw_animals(self, screen):
        for animal in self.animals:
            if animal['type'] == 'deer':
                pygame.draw.rect(screen, (200, 100, 0), (animal['x'], animal['y'], 25, 20))
            else:  # wolf
                pygame.draw.rect(screen, (100, 0, 0), (animal['x'], animal['y'], 25, 20))
