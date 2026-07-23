import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
pygame.init()
class Key:
    def __init__(self, note, color, x, y, font):
        self.note = note
        self.sound = pygame.mixer.Sound(rf"Notes\{note}.mp3")
        self.color = color
        self.x = x
        self.y = y
        self.width = 30
        self.length = 300 if self.color == WHITE else 230
        self.text = font.render(self.note, True, BLACK if self.color == WHITE else WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x + self.width / 2, self.y + self.length / 2)

    def show(self, screen, clicked, mouse_pos, cooldown):
        if self.clicked(clicked, mouse_pos) and cooldown < 0:
            pygame.draw.rect(screen, self.color, (self.x, self.y + 10, self.width, self.length))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.length))
        screen.blit(self.text, self.text_rect)

    def clicked(self, clicked, mouse_pos):
        if clicked:
            if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.length:
                return True
        return False

    def playnote(self, clicked, mouse_pos, cooldown):
        if self.clicked(clicked, mouse_pos) and cooldown < 0:
            self.sound.play()
            return True, self.note, 10
        return False, self.note, cooldown