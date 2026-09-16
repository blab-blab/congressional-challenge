import pygame


class GuessTheNoteButton:
    def __init__(self, x, y, width, length, color, font, button_image, button_hover_image, text_color, screen):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.color = color
        self.font = font
        self.button_image = button_image
        self.button_hover_image = button_hover_image
        self.text_color = text_color
        self.screen = screen
        self.text = self.font.render("PLAY", True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + self.width / 2, self.y + self.length / 2)

    def hovered(self, mouse_pos):
        return (
            mouse_pos[0] > self.x
            and mouse_pos[0] < self.x + self.width
            and mouse_pos[1] > self.y
            and mouse_pos[1] < self.y + self.length
        )

    def show(self, mouse_pos):
        if self.hovered(mouse_pos):
            self.screen.blit(self.button_hover_image, (self.x - 5, self.y - 5))
        else:
            self.screen.blit(self.button_image, (self.x, self.y))

    def clicked(self, clicked, mouse_pos):
        if clicked and self.hovered(mouse_pos):
            return True
        return False

