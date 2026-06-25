import pygame
import numpy as np
import time


# 1. Initialize the mixer with specific audio settings
pygame.init()
# sample_rate = 44100
# pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)

# def generate_note(frequency, duration, volume=0.5):
#     """Generates a raw sound buffer for a specific frequency."""
#     num_samples = int(sample_rate * duration)

#     # Calculate a sine wave array
#     t = np.linspace(0, duration, num_samples, False)
#     wave = np.sin(2 * np.pi * frequency * t)

#     # Convert float wave to a 16-bit signed integer array
#     audio_buffer = (wave * volume * 32767).astype(np.int16)

#     # Return a Pygame Sound object
#     return pygame.mixer.Sound(buffer=audio_buffer)

# # 2. Create an A4 note (440Hz) lasting for 1.5 seconds
# note_a4 = generate_note(frequency=116.54, duration=1.5)

# # 3. Play the note
# print("Playing 440Hz Tone...")
# note_a4.play()

# # Keep the script alive while the sound plays
# time.sleep(1.5)
# pygame.quit()

WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BEIGE = (237,232,208)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("Open Sans", 30)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blank Pygame Template")
clock = pygame.time.Clock()


notes = ["C","D","E","F","G","A","B"]



pygame.mixer.init()

c3 = pygame.mixer.Sound(r"Notes\C3.mp3")
# for i in range(3,7):




class Key:
    def __init__(self,note,color):
        self.note = note
        self.color = color
        self.x = 400
        self.y = 300
        self.width = 30
        self.length = 300
        self.text = font.render(self.note, True, WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x+self.width/2,self.y+self.length/2)
    def show(self):
        if self.clicked():
            pygame.draw.rect(screen, self.color, (self.x, self.y+10, self.width, self.length))
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.length))
        screen.blit(self.text,self.text_rect)
    def clicked(self):
        if clicked == True:
            if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.length:
                return True
        return False
    def playnote(self):
        if self.clicked():
            c3.play()
clicked = False
mouse_pos = (0,0)
running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
                mouse_pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False
                mouse_pos = event.pos 
            
    # 2. Update Game State
    
    # 3. Draw
    screen.fill(BEIGE)
    key = Key("C3", BLACK)
    key.show()
    key.playnote()
        # time.sleep(2.0)
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)
    




