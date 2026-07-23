import pygame
import button
import time
class ToggleButton(button.GameButton):
    def __init__(self, x, y, width, length, color, font, button_image, button_hover_image, text_color, screen,note):
        super().__init__(x, y, width, length, color, font, button_image, button_hover_image, text_color, screen)
        self.text = self.font.render(note, True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + self.width / 2, self.y + self.length / 2)
        self.toggled = False

    def clicked(self, clicked, mouse_pos):
        if clicked and self.hovered(mouse_pos):
            self.toggled = not self.toggled
            time.sleep(0.1)  # Add a small delay to prevent rapid toggling
            return True
        return False

    def show(self, mouse_pos):
        if self.toggled:
            self.screen.blit(self.button_hover_image, (self.x, self.y))
        else:
            self.screen.blit(self.button_image, (self.x, self.y))
        self.screen.blit(self.text, (self.x+25,self.y+5))