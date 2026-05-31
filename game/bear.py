import pygame
import math

class Bear:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 2
        self.awake = False
        self.target_player = None
        self.health = 200
        
    def update(self, time_system, target_player):
        self.target_player = target_player
        
        # Bear only awake at night
        if time_system.is_night():
            self.awake = True
            self.chase_player()
        else:
            self.awake = False
            self.wander()
    
    def chase_player(self):
        if self.target_player:
            dx = self.target_player.x - self.x
            dy = self.target_player.y - self.y
            distance = math.sqrt(dx**2 + dy**2)
            
            if distance > 0:
                self.x += (dx / distance) * self.speed
                self.y += (dy / distance) * self.speed
    
    def wander(self):
        # Slow random walk during day
        import random
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)
    
    def check_collision(self, player):
        bear_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
        return bear_rect.colliderect(player_rect)
    
    def draw(self, screen, time_system):
        color = (139, 69, 19) if self.awake else (101, 50, 15)  # Darker when sleeping
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        # Draw eyes
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x + 12), int(self.y + 10)), 3)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x + 38), int(self.y + 10)), 3)
