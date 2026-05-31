import pygame

class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font_large = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)
    
    def draw(self, screen, players, time_system):
        # Draw time info
        time_text = self.font_large.render(time_system.get_time_string(), True, (255, 255, 255))
        screen.blit(time_text, (10, 10))
        
        # Day/Night indicator
        day_night = "NIGHT (Dangerous!)" if time_system.is_night() else "DAY (Safe)"
        day_night_color = (255, 0, 0) if time_system.is_night() else (255, 255, 0)
        day_night_text = self.font_small.render(day_night, True, day_night_color)
        screen.blit(day_night_text, (10, 50))
        
        # Player stats
        y_offset = 100
        for i, player in enumerate(players):
            player_info = f"Player {player.player_id}: HP {player.health:.0f} | Hunger {player.hunger:.0f} | Thirst {player.thirst:.0f}"
            info_text = self.font_small.render(player_info, True, (255, 255, 255))
            screen.blit(info_text, (10, y_offset + i * 30))
        
        # Controls
        controls = [
            "WASD: Move | E: Interact | C: Cook | SPACE: Sleep | ESC: Pause",
            "Survive 99 nights! Stay in bed at night!"
        ]
        
        for i, control in enumerate(controls):
            control_text = self.font_small.render(control, True, (200, 200, 200))
            screen.blit(control_text, (10, self.height - 70 + i * 25))
        
        # Survival nights counter
        nights_text = self.font_large.render(f"Nights Survived: {time_system.days}/99", True, (0, 255, 0))
        screen.blit(nights_text, (self.width - 350, 10))
    
    def draw_pause_menu(self, screen):
        # Semi-transparent overlay
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = self.font_large.render("PAUSED", True, (255, 255, 255))
        text_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
        screen.blit(pause_text, text_rect)
        
        resume_text = self.font_small.render("Press ESC to resume", True, (200, 200, 200))
        resume_rect = resume_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
        screen.blit(resume_text, resume_rect)
