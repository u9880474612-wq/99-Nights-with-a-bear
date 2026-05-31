import pygame
import math
import random

class Bear(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 50
        self.height = 60
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((101, 67, 33))  # Dark brown
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.awake = False
        self.speed = 3
        self.detection_range = 200
        self.health = 150
        self.attack_cooldown = 0
    
    def update(self, time_system, player):
        if time_system.is_night():
            self.awake = True
        else:
            self.awake = False
            self.x = self.rect.x  # Stay in cave during day
            return
        
        # Bear AI when awake at night
        if self.awake:
            dx = player.x - self.x
            dy = player.y - self.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance < self.detection_range:
                # Move toward player
                if distance > 0:
                    self.x += (dx / distance) * self.speed
                    self.y += (dy / distance) * self.speed
                    self.rect.x = self.x
                    self.rect.y = self.y
            else:
                # Random patrolling in cave
                if random.random() < 0.02:
                    self.x += random.randint(-2, 2)
                    self.y += random.randint(-2, 2)
                    self.rect.x = self.x
                    self.rect.y = self.y
        
        # Update attack cooldown
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
    
    def check_collision(self, player):
        return self.rect.colliderect(player.rect)
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"Bear took {damage} damage! Health: {self.health}")
    
    def draw(self, screen, time_system):
        if self.awake:
            color = (150, 50, 50)  # Reddish when angry
        else:
            color = (101, 67, 33)  # Normal brown when sleeping
        
        pygame.draw.ellipse(screen, color, (self.x, self.y, self.width, self.height))
        
        # Draw eyes
        eye_color = (255, 255, 255) if self.awake else (100, 100, 100)
        pygame.draw.circle(screen, eye_color, (int(self.x + 15), int(self.y + 15)), 4)
        pygame.draw.circle(screen, eye_color, (int(self.x + 35), int(self.y + 15)), 4)
        
        # Draw pupils
        pupil_color = (0, 0, 0)
        pygame.draw.circle(screen, pupil_color, (int(self.x + 15), int(self.y + 15)), 2)
        pygame.draw.circle(screen, pupil_color, (int(self.x + 35), int(self.y + 15)), 2)
        
        # Draw snout
        pygame.draw.circle(screen, (70, 40, 20), (int(self.x + 25), int(self.y + 40)), 6)
