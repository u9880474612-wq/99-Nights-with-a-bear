import pygame
import random
import math

class Animal(pygame.sprite.Sprite):
    def __init__(self, x, y, animal_type):
        super().__init__()
        self.x = x
        self.y = y
        self.animal_type = animal_type  # "deer", "rabbit", "wolf"
        self.width = 30 if animal_type != "wolf" else 40
        self.height = 25 if animal_type != "wolf" else 35
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.speed = 2
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Set color based on type
        if animal_type == "deer":
            self.color = (139, 69, 19)  # Brown
        elif animal_type == "rabbit":
            self.color = (200, 200, 150)  # Light brown
        elif animal_type == "wolf":
            self.color = (100, 100, 100)  # Gray
        
        self.health = 50 if animal_type == "deer" else (20 if animal_type == "rabbit" else 60)
        self.aggression = 0 if animal_type != "wolf" else 8
    
    def update(self, world_width, world_height):
        self.x += self.vx * self.speed
        self.y += self.vy * self.speed
        
        # Bounce off edges
        if self.x < 0 or self.x > world_width:
            self.vx *= -1
        if self.y < 0 or self.y > world_height:
            self.vy *= -1
        
        # Random movement changes
        if random.random() < 0.02:
            self.vx = random.uniform(-1, 1)
            self.vy = random.uniform(-1, 1)
        
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.width, self.height))


class Tree:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 80
        self.health = health
        self.rect = pygame.Rect(x, y, self.width, self.height)
    
    def draw(self, screen):
        # Trunk
        pygame.draw.rect(screen, (101, 67, 33), (self.x + 10, self.y + 40, 20, 40))
        # Leaves
        pygame.draw.circle(screen, (34, 139, 34), (int(self.x + 20), int(self.y + 30)), 25)
    
    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0


class Chest:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.opened = False
        self.loot = self._generate_loot()
    
    def _generate_loot(self):
        loot = []
        items = ["cooked_meat", "fish", "vegetable", "wood", "stone", "gold_coin"]
        for _ in range(random.randint(3, 6)):
            loot.append(random.choice(items))
        return loot
    
    def open(self):
        self.opened = True
        return self.loot
    
    def draw(self, screen):
        color = (218, 165, 32) if not self.opened else (160, 120, 20)
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cave_x = 50
        self.cave_y = 50
        self.cave_width = 300
        self.cave_height = 200
        
        # Generate world features
        self.trees = [Tree(random.randint(400, width-100), random.randint(100, height-100)) for _ in range(15)]
        self.animals = [Animal(random.randint(400, width-100), random.randint(100, height-100), 
                              random.choice(["deer", "rabbit", "wolf"])) for _ in range(12)]
        self.chests = [Chest(random.randint(400, width-200), random.randint(150, height-150)) for _ in range(5)]
        
        # Water
        self.water_x = width - 200
        self.water_y = height - 150
        self.water_width = 150
        self.water_height = 100
        
        # Hidden button for cave door
        self.button_x = 100
        self.button_y = 120
        self.button_width = 20
        self.button_height = 20
        self.door_open = False
    
    def is_walkable(self, x, y, width, height):
        # Check if position collides with obstacles
        rect = pygame.Rect(x, y, width, height)
        
        # Can't walk in trees
        for tree in self.trees:
            if rect.colliderect(tree.rect):
                return False
        
        # Can walk anywhere else
        return True
    
    def check_button_press(self, player_rect):
        button_rect = pygame.Rect(self.button_x, self.button_y, self.button_width, self.button_height)
        if player_rect.colliderect(button_rect):
            self.door_open = not self.door_open
            return True
        return False
    
    def update(self, time_system):
        for animal in self.animals:
            animal.update(self.width, self.height)
    
    def draw(self, screen):
        # Draw cave
        pygame.draw.rect(screen, (50, 50, 50), (self.cave_x, self.cave_y, self.cave_width, self.cave_height))
        
        # Draw cave door (big rock)
        if not self.door_open:
            pygame.draw.rect(screen, (100, 100, 100), (self.cave_x + 130, self.cave_y + 50, 50, 80))
        
        # Draw hidden button
        button_color = (0, 255, 0) if self.door_open else (150, 0, 0)
        pygame.draw.rect(screen, button_color, (self.button_x, self.button_y, self.button_width, self.button_height))
        
        # Draw trees
        for tree in self.trees:
            tree.draw(screen)
        
        # Draw chests
        for chest in self.chests:
            chest.draw(screen)
        
        # Draw water
        pygame.draw.rect(screen, (0, 150, 255), (self.water_x, self.water_y, self.water_width, self.water_height))
    
    def draw_animals(self, screen):
        for animal in self.animals:
            animal.draw(screen)
