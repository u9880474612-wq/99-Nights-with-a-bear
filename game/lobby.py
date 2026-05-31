import pygame

class Lobby:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.num_players = 1
        self.max_players = 5
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 32)
        self.font_small = pygame.font.Font(None, 24)
    
    def add_player(self):
        if self.num_players < self.max_players:
            self.num_players += 1
    
    def remove_player(self):
        if self.num_players > 1:
            self.num_players -= 1
    
    def update(self):
        # Lobby is simple, no complex updates needed
        pass
    
    def draw(self, screen):
        # Draw background
        screen.fill((34, 139, 34))
        
        # Draw title
        title_text = self.font_large.render("99 Nights with a Bear", True, (255, 255, 255))
        screen.blit(title_text, (self.width // 2 - 300, 50))
        
        # Draw subtitle
        subtitle_text = self.font_medium.render("Multiplayer Survival Game", True, (200, 200, 100))
        screen.blit(subtitle_text, (self.width // 2 - 220, 120))
        
        # Draw player selection
        player_select_text = self.font_medium.render("Select Number of Players:", True, (255, 255, 255))
        screen.blit(player_select_text, (self.width // 2 - 280, 250))
        
        # Draw player count with visual display
        for i in range(1, self.max_players + 1):
            x = self.width // 2 - 150 + i * 60
            y = 330
            
            if i == self.num_players:
                color = (0, 255, 0)  # Green for selected
                pygame.draw.circle(screen, color, (x, y), 25, 3)
            else:
                color = (100, 100, 100)  # Gray for not selected
                pygame.draw.circle(screen, color, (x, y), 25, 2)
            
            number_text = self.font_medium.render(str(i), True, color)
            screen.blit(number_text, (x - 15, y - 20))
        
        # Draw instructions
        up_text = self.font_small.render("UP Arrow: Add Player", True, (200, 200, 200))
        screen.blit(up_text, (self.width // 2 - 200, 450))
        
        down_text = self.font_small.render("DOWN Arrow: Remove Player", True, (200, 200, 200))
        screen.blit(down_text, (self.width // 2 - 200, 490))
        
        # Draw start button
        start_text = self.font_medium.render("PRESS SPACE TO START", True, (0, 255, 100))
        pygame.draw.rect(screen, (0, 100, 50), (self.width // 2 - 250, 580, 500, 60), 3)
        screen.blit(start_text, (self.width // 2 - 240, 595))
        
        # Draw game info
        info_text = self.font_small.render("Survive 99 nights with a bear in the forest!", True, (100, 200, 255))
        screen.blit(info_text, (self.width // 2 - 350, 700))
