import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Bomb(Sprite):
    """A class to manage bombs dropped from the ship."""

    def __init__(self, ai_game):
        """Create a bomb object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bomb_color

        # Create a bomb rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bomb_diameter,
            self.settings.bomb_diameter)
        self.rect.midbottom = ai_game.ship.rect.midbottom

        # Store the bomb's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bomb down the screen."""
        # Update the exact position of the bomb.
        self.y += self.settings.bomb_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bomb(self):
        """Draw the bomb to the screen."""
        pygame.draw.circle(self.screen, self.color, self.rect.center, self.settings.bomb_diameter // 2)

    def detonate(self, enemies):
        """Detonate the bomb and kill adjacent enemies."""
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemies.remove(enemy)
                # Check for adjacent enemies
                for adj_enemy in enemies.copy():
                    if self.rect.inflate(self.settings.bomb_explosion_radius, self.settings.bomb_explosion_radius).colliderect(adj_enemy.rect):
                        enemies.remove(adj_enemy)