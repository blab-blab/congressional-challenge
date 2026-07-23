import pygame
import time

class GameButton:
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
            self.screen.blit(self.button_hover_image, (self.x - 10, self.y - 10))
        else:
            self.screen.blit(self.button_image, (self.x, self.y))

    def clicked(self, clicked, mouse_pos):
        if clicked and self.hovered(mouse_pos):
            time.sleep(0.1)  # Add a small delay to prevent rapid toggling
            return True
        return False

    def validate_note(self, note, correct_note, screen, confetti_particles, confetti_colors, width):
        if note == correct_note:
            self.text = self.font.render("Correct note!", True, (0, 0, 0))
            screen.blit(self.text, (self.x, self.y))
            from confetti import spawn_confetti
            spawn_confetti(width // 2, 100, 5, confetti_particles, confetti_colors)
        else:
            self.text = self.font.render(
                f"Incorrect note! The correct note was {correct_note}", True, (0, 0, 0)
            )
            screen.blit(self.text, (self.x, self.y))
