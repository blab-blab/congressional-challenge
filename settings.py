import pygame
import button

class SettingsButton(button.GameButton):
    def __init__(self, x, y, width, length, color, font, button_image, button_hover_image, text_color, screen):
        super().__init__(x, y, width, length, color, font, button_image, button_hover_image, text_color, screen)
        self.text = self.font.render("SETTINGS", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + self.width / 2, self.y + self.length / 2)

    def show(self, mouse_pos):
        if self.hovered(mouse_pos):
            self.screen.blit(self.button_hover_image, (self.x - 5, self.y - 5))
        else:
            self.screen.blit(self.button_image, (self.x, self.y))