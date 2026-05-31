import pygame
import sys
import random
from game.player import Player
from game.world import World
from game.bear import Bear
from game.time_system import TimeSystem
from game.inventory import Inventory
from game.ui import UI
from game.lobby import Lobby

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
        
        # Game state
        self.state = "lobby"  # lobby, game, game_over
        self.lobby = Lobby(self.width, self.height)
        
        # Game variables (initialized after lobby)
        self.time_system = None
        self.world = None
        self.players = []
        self.bear = None
        self.ui = None
        self.paused = False
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.state == "lobby":
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                    elif event.key == pygame.K_UP:
                        self.lobby.add_player()
                    elif event.key == pygame.K_DOWN:
                        self.lobby.remove_player()
                elif self.state == "game":
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused
                    elif event.key == pygame.K_e:
                        for player in self.players:
                            player.interact(self.world, player.inventory)
                    elif event.key == pygame.K_c:
                        for player in self.players:
                            player.cook_food(player.inventory)
                    elif event.key == pygame.K_SPACE:
                        for player in self.players:
                            if player.in_bed and self.time_system.is_night():
                                player.sleep(self.time_system)
    
    def start_game(self):
        """Initialize game with selected number of players"""
        num_players = self.lobby.num_players
        
        self.time_system = TimeSystem()
        self.world = World(self.width, self.height)
        self.bear = Bear(self.world.cave_x + 150, self.world.cave_y + 100)
        self.ui = UI(self.width, self.height)
        
        # Create players with spawn positions around the fence in the forest
        spawn_positions = self.get_spawn_positions(num_players)
        self.players = []
        for i, (x, y) in enumerate(spawn_positions):
            player = Player(x, y)
            player.player_id = i + 1
            player.inventory = Inventory()
            self.players.append(player)
        
        self.state = "game"
    
    def get_spawn_positions(self, num_players):
        """Get spawn positions around the forest fence"""
        fence_center_x = self.world.fence_center_x
        fence_center_y = self.world.fence_center_y
        fence_radius = self.world.fence_radius
        
        positions = []
        for i in range(num_players):
            angle = (2 * 3.14159 * i) / num_players  # Distribute players around fence
            x = fence_center_x + fence_radius * 0.7 * pygame.math.cos(angle)
            y = fence_center_y + fence_radius * 0.7 * pygame.math.sin(angle)
            positions.append((x, y))
        
        return positions
    
    def update(self):
        if self.state == "lobby":
            self.lobby.update()
        elif self.state == "game" and not self.paused:
            keys = pygame.key.get_pressed()
            
            # Player movement (support multiple players with different keys)
            if keys[pygame.K_w]:
                for player in self.players:
                    player.move(0, -5, self.world)
            if keys[pygame.K_s]:
                for player in self.players:
                    player.move(0, 5, self.world)
            if keys[pygame.K_a]:
                for player in self.players:
                    player.move(-5, 0, self.world)
            if keys[pygame.K_d]:
                for player in self.players:
                    player.move(5, 0, self.world)
            
            # Update time system
            self.time_system.update()
            
            # Update bear behavior
            # Bear targets closest player
            closest_player = min(self.players, key=lambda p: ((p.x - self.bear.x)**2 + (p.y - self.bear.y)**2)**0.5)
            self.bear.update(self.time_system, closest_player)
            
            # Update world
            self.world.update(self.time_system)
            
            # Update all players
            for player in self.players:
                player.update(self.time_system, player.inventory)
                
                # Check bear collision
                if self.bear.check_collision(player) and not player.in_bed:
                    player.take_damage(5)
            
            # Check win/lose conditions
            self.check_game_status()
    
    def check_game_status(self):
        all_dead = all(player.health <= 0 for player in self.players)
        
        if all_dead:
            print("Game Over! All players were caught!")
            self.state = "game_over"
            self.running = False
        elif self.time_system.days >= 99:
            print("You all survived 99 nights! You win!")
            self.state = "game_over"
            self.running = False
    
    def draw(self):
        self.screen.fill((34, 139, 34))  # Forest green background
        
        if self.state == "lobby":
            self.lobby.draw(self.screen)
        elif self.state == "game":
            # Draw world elements
            self.world.draw(self.screen)
            
            # Draw animals
            self.world.draw_animals(self.screen)
            
            # Draw all players
            for player in self.players:
                player.draw(self.screen)
            
            # Draw bear
            self.bear.draw(self.screen, self.time_system)
            
            # Draw UI
            self.ui.draw(self.screen, self.players, self.time_system)
            
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
