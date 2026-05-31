import pygame

class Lobby:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.num_players = 1
        self.max_players = 4
        self.font_large = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
    
    def add_player(self):
        if self.num_players < self.max_players:
            self.num_players += 1
    
    def remove_player(self):
        if self.num_players > 1:
            self.num_players -= 1
    
    def update(self):
        pass
    
    def draw(self, screen):
        screen.fill((34, 139, 34))
        
        # Title
        title = self.font_large.render("99 NIGHTS WITH A BEAR", True, (255, 255, 0))
        title_rect = title.get_rect(center=(self.width // 2, 50))
        screen.blit(title, title_rect)
        
        # Subtitle
        subtitle = self.font_medium.render("Survival Game", True, (255, 255, 255))
        subtitle_rect = subtitle.get_rect(center=(self.width // 2, 120))
        screen.blit(subtitle, subtitle_rect)
        
        # Instructions
        instructions = [
            f"Players: {self.num_players}",
            "UP/DOWN: Change player count",
            "SPACE: Start Game"
        ]
        
        y = 250
        for instruction in instructions:
            inst_text = self.font_medium.render(instruction, True, (200, 200, 200))
            inst_rect = inst_text.get_rect(center=(self.width // 2, y))
            screen.blit(inst_text, inst_rect)
            y += 60
        
        # Game info
        info = [
            "Survive 99 nights with a bear in the cave!",
            "Manage hunger, thirst, and health.",
            "Hunt animals, gather resources, and cook food.",
            "Sleep in bed at night to avoid the bear."
        ]
        
        y = 550
        for line in info:
            info_text = self.font_small.render(line, True, (200, 200, 100))
            info_rect = info_text.get_rect(center=(self.width // 2, y))
            screen.blit(info_text, info_rect)
            y += 30
