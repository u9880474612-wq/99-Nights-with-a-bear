import pygame

class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font_large = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 24)
        self.font_small = pygame.font.Font(None, 18)
    
    def draw(self, screen, player, time_system, inventory):
        # Draw health bar
        health_text = self.font_small.render(f"Health: {int(player.health)}/100", True, (255, 0, 0))
        screen.blit(health_text, (10, 10))
        pygame.draw.rect(screen, (255, 0, 0), (10, 30, player.health * 2, 20))
        pygame.draw.rect(screen, (255, 255, 255), (10, 30, 200, 20), 2)
        
        # Draw hunger bar
        hunger_text = self.font_small.render(f"Hunger: {int(player.hunger)}/100", True, (255, 165, 0))
        screen.blit(hunger_text, (10, 60))
        pygame.draw.rect(screen, (255, 165, 0), (10, 80, player.hunger * 2, 20))
        pygame.draw.rect(screen, (255, 255, 255), (10, 80, 200, 20), 2)
        
        # Draw energy bar
        energy_text = self.font_small.render(f"Energy: {int(player.energy)}/100", True, (0, 150, 255))
        screen.blit(energy_text, (10, 110))
        pygame.draw.rect(screen, (0, 150, 255), (10, 130, player.energy * 2, 20))
        pygame.draw.rect(screen, (255, 255, 255), (10, 130, 200, 20), 2)
        
        # Draw time
        time_text = self.font_medium.render(f"Time: {time_system.get_time_string()} - Day {time_system.days}", True, (255, 255, 255))
        screen.blit(time_text, (self.width - 300, 10))
        
        # Draw day phase
        phase_text = self.font_small.render(time_system.get_day_phase(), True, (255, 255, 100))
        screen.blit(phase_text, (self.width - 300, 40))
        
        # Draw inventory
        inv_counts = inventory.get_item_counts()
        inv_text = self.font_small.render(f"Inventory ({len(inventory.items)}/{inventory.max_size})", True, (200, 200, 200))
        screen.blit(inv_text, (10, self.height - 150))
        
        y_offset = self.height - 120
        for item, count in inv_counts.items():
            item_text = self.font_small.render(f"  {item}: {count}", True, (150, 200, 150))
            screen.blit(item_text, (10, y_offset))
            y_offset += 25
        
        # Draw controls
        controls = [
            "WASD: Move | E: Interact | C: Cook",
            "SPACE: Sleep (in bed at night) | ESC: Pause"
        ]
        for i, control in enumerate(controls):
            control_text = self.font_small.render(control, True, (200, 200, 200))
            screen.blit(control_text, (10, self.height - 40 + i * 20))
    
    def draw_pause_menu(self, screen):
        # Semi-transparent overlay
        overlay = pygame.Surface((self.width, self.height))
        overlay.set_alpha(128)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = self.font_large.render("PAUSED", True, (255, 255, 255))
        screen.blit(pause_text, (self.width // 2 - 100, self.height // 2 - 50))
        
        resume_text = self.font_medium.render("Press ESC to Resume", True, (200, 200, 200))
        screen.blit(resume_text, (self.width // 2 - 150, self.height // 2 + 20))
