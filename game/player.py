import pygame
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 30
        self.height = 40
        self.health = 100
        self.hunger = 100
        self.energy = 100
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((200, 100, 50))  # Brown skin color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.in_bed = False
        self.inventory = []
        self.speed = 5
        
    def move(self, dx, dy, world):
        # Check boundaries and obstacles
        new_x = self.x + dx
        new_y = self.y + dy
        
        if world.is_walkable(new_x, new_y, self.width, self.height):
            self.x = new_x
            self.y = new_y
            self.rect.x = self.x
            self.rect.y = self.y
    
    def interact(self, world, inventory):
        # Interact with nearby objects (chests, animals, etc.)
        for chest in world.chests:
            if self.rect.colliderect(chest.rect):
                items = chest.open()
                inventory.add_items(items)
                print(f"Found items in chest: {items}")
    
    def cook_food(self, inventory):
        raw_meat = inventory.count("raw_meat")
        if raw_meat > 0:
            inventory.remove("raw_meat")
            inventory.add("cooked_meat")
            self.hunger = min(self.hunger + 30, 100)
            print("Cooked meat and ate it!")
        else:
            print("No raw meat to cook!")
    
    def eat(self, food_type, inventory):
        if inventory.has(food_type):
            inventory.remove(food_type)
            if food_type == "cooked_meat":
                self.hunger = min(self.hunger + 40, 100)
            elif food_type == "fish":
                self.hunger = min(self.hunger + 35, 100)
            elif food_type == "vegetable":
                self.hunger = min(self.hunger + 20, 100)
            print(f"Ate {food_type}! Hunger: {self.hunger}")
    
    def sleep(self, time_system):
        if self.in_bed and time_system.is_night():
            self.energy = 100
            self.hunger = max(self.hunger - 10, 0)
            time_system.skip_night()
            print("Slept through the night safely!")
    
    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)
        print(f"Player took {damage} damage! Health: {self.health}")
    
    def update(self, time_system, inventory):
        # Decrease stats over time
        self.hunger = max(self.hunger - 0.1, 0)
        self.energy = max(self.energy - 0.05, 0)
        
        if self.hunger < 30:
            self.take_damage(0.5)
            print("Starving...")
    
    def draw(self, screen):
        pygame.draw.rect(screen, (200, 100, 50), (self.x, self.y, self.width, self.height))
        # Draw eyes
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x + 8), int(self.y + 10)), 3)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x + 22), int(self.y + 10)), 3)
