# Button
import pygame
class Button:
    def __init__(self, x, y, image, scale, hover_scale=0.9, hover_enabled=True):
        width = image.get_width()
        height = image.get_height()
        self.original_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.hover_scale = hover_scale
        self.is_hovered = False
        self.hover_enabled = hover_enabled
    def draw(self,surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if self.hover_enabled and not self.is_hovered:
                self.is_hovered = True
                width = self.original_image.get_width()
                height = self.original_image.get_height()
                self.image = pygame.transform.scale(
                    self.original_image,
                    (int(width * self.hover_scale), int(height * self.hover_scale))
                )
                self.rect = self.image.get_rect(center=self.rect.center)
            # Check for click
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        else:
            if self.is_hovered and self.hover_enabled:
                self.is_hovered = False
                center = self.rect.center
                self.image = self.original_image
                self.rect = self.image.get_rect(center=center)
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, self.rect.topleft)
        return action