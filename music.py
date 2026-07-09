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
image = pygame.image.load(r"C:\Users\sanfr\Documents\carl\images\sound.png")
image = pygame.transform.scale(image, (50,50))
# Colors
BEIGE = (237,232,208)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255,179,71)

font = pygame.font.SysFont("Open Sans", 30)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blank Pygame Template")
clock = pygame.time.Clock()
cooldown = 0

notes = ["C","D","E","F","G","A","B"]
a = ["D","E","G","A","B"]
normalnotes = []
accidentals = []
for i in range (2,5):
    for j in range(len(notes)):
        normalnotes.append(notes[j] + str(i))
    for j in range(len(a)):
        accidentals.append(a[j] + "b" + str(i))


pygame.mixer.init()




class GameButton:
    def __init__(self):
        self.x = 100
        self.y = 200
        self.width = 100
        self.length = 75
        self.text = font.render("PLAY", True, ORANGE)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x+self.width/2,self.y+self.length/2)

    def show(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.length))
        screen.blit(self.text,self.text_rect)
    def clicked(self):
        if clicked == True:
            if mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height:
                return True
        return False

class Key:
    def __init__(self,note,color,x,y):
        self.note = note
        self.sound = pygame.mixer.Sound(rf"Notes\{note}.mp3")
        self.color = color
        self.x = x
        self.y = y
        self.width = 30
        self.length = 300 if self.color == WHITE else 230
        self.text = font.render(self.note, True, BLACK if self.color == WHITE else WHITE)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x+self.width/2,self.y+self.length/2)
    def show(self):
        if self.clicked() and cooldown < 0:
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
        global cooldown
        if self.clicked() and cooldown < 0:
            self.sound.play()
            cooldown = 10
clicked = False
mouse_pos = (0,0)
running = True
keysWHITE = []
keysBLACK = []
x = 50
for i in range(21):
    keysWHITE.append(Key(normalnotes[i], WHITE,i*35+30,300))
for i in range(15):
    keysBLACK.append(Key(accidentals[i],BLACK, x, 200))
    if accidentals[i][0] == "E" or accidentals[i][0] == "B":
        x += 35
    x+=35

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
    cooldown -= 1

    for key in keysWHITE:
        key.show()
    for key in keysBLACK:
        key.show()

    for key in keysBLACK:
        key.playnote()
    for key in keysWHITE:
        key.playnote()
        # time.sleep(2.0)


    screen.blit(image, (0,0))
    # Update the display
    pygame.display.flip()
    
    #to show the image
    
    # Cap the frame rate
    clock.tick(FPS)
    
    




