import pygame
import sys
import random
from game.player import Player
from game.world import World
from game.bear import Bear
from game.time_system import TimeSystem
from game.inventory import Inventory
from game.ui import UI

class Game:
    def __init__(self):
        pygame.init()
        self.width = 1200
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("99 Nights with a Bear - Survival Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.fps = 60
        
        # Initialize game systems
        self.time_system = TimeSystem()
        self.world = World(self.width, self.height)
        self.player = Player(100, 100)
        self.bear = Bear(self.world.cave_x, self.world.cave_y)
        self.inventory = Inventory()
        self.ui = UI(self.width, self.height)
        
        self.paused = False
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
                elif event.key == pygame.K_e:
                    self.player.interact(self.world, self.inventory)
                elif event.key == pygame.K_c:
                    self.player.cook_food(self.inventory)
                elif event.key == pygame.K_SPACE:
                    if self.player.in_bed and self.time_system.is_night():
                        self.player.sleep(self.time_system)
    
    def update(self):
        if not self.paused:
            keys = pygame.key.get_pressed()
            
            # Player movement
            if keys[pygame.K_w]:
                self.player.move(0, -5, self.world)
            if keys[pygame.K_s]:
                self.player.move(0, 5, self.world)
            if keys[pygame.K_a]:
                self.player.move(-5, 0, self.world)
            if keys[pygame.K_d]:
                self.player.move(5, 0, self.world)
            
            # Update time system
            self.time_system.update()
            
            # Update bear behavior based on time
            self.bear.update(self.time_system, self.player)
            
            # Update world elements
            self.world.update(self.time_system)
            
            # Update player status
            self.player.update(self.time_system, self.inventory)
            
            # Check for bear collision
            if self.bear.check_collision(self.player) and not self.player.in_bed:
                self.player.take_damage(5)
                print(f"Bear attacks! Health: {self.player.health}")
            
            # Check win/lose conditions
            self.check_game_status()
    
    def check_game_status(self):
        if self.player.health <= 0:
            print("Game Over! You were caught by the bear!")
            self.running = False
        elif self.time_system.days >= 99:
            print("You survived 99 nights! You win!")
            self.running = False
    
    def draw(self):
        self.screen.fill((34, 139, 34))  # Forest green background
        
        # Draw world elements
        self.world.draw(self.screen)
        
        # Draw animals
        self.world.draw_animals(self.screen)
        
        # Draw player
        self.player.draw(self.screen)
        
        # Draw bear
        self.bear.draw(self.screen, self.time_system)
        
        # Draw UI
        self.ui.draw(self.screen, self.player, self.time_system, self.inventory)
        
        if self.paused:
            self.ui.draw_pause_menu(self.screen)
        
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
