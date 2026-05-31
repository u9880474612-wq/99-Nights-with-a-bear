import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 30
        self.health = 100
        self.hunger = 100
        self.thirst = 100
        self.speed = 5
        self.player_id = 1
        self.inventory = None
        self.in_bed = False
        self.bed_x = 0
        self.bed_y = 0
        
    def move(self, dx, dy, world):
        new_x = self.x + dx
        new_y = self.y + dy
        
        # Check boundaries
        if 0 <= new_x <= world.width - self.width and 0 <= new_y <= world.height - self.height:
            self.x = new_x
            self.y = new_y
    
    def update(self, time_system, inventory):
        # Decrease hunger and thirst over time
        self.hunger -= 0.02
        self.thirst -= 0.03
        
        # Starving and dying from thirst
        if self.hunger <= 0:
            self.health -= 1
        if self.thirst <= 0:
            self.health -= 2
        
        # Cap values
        self.hunger = max(0, min(100, self.hunger))
        self.thirst = max(0, min(100, self.thirst))
        self.health = max(0, self.health)
    
    def take_damage(self, amount):
        self.health -= amount
    
    def interact(self, world, inventory):
        # Check if near objects to interact with
        pass
    
    def cook_food(self, inventory):
        if inventory.raw_meat > 0:
            inventory.raw_meat -= 1
            inventory.cooked_meat += 1
            print(f"Player {self.player_id} cooked meat")
    
    def sleep(self, time_system):
        self.in_bed = True
        self.hunger -= 5
        self.health += 10
        self.health = min(100, self.health)
        print(f"Player {self.player_id} slept through the night")
        time_system.advance_day()
    
    def eat(self, inventory):
        if inventory.cooked_meat > 0:
            inventory.cooked_meat -= 1
            self.hunger = min(100, self.hunger + 50)
    
    def drink(self):
        self.thirst = 100
    
    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.width, self.height))
        # Draw player ID
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.player_id), True, (255, 255, 255))
        screen.blit(text, (self.x + 5, self.y + 5))
