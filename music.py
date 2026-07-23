import pygame
import numpy as np
import time
import random
from guessthenote import GuessTheNoteButton
from key import Key
from button import GameButton
from confetti import spawn_confetti
from settings import SettingsButton
from togglebutton import ToggleButton
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
image = pygame.image.load(r"C:\Users\noobp\Documents\congressional-challenge\images\sound.png")
image = pygame.transform.scale(image, (50,50))

button = pygame.image.load(r"C:\Users\noobp\Documents\congressional-challenge\images\playbutton.png")
button = pygame.transform.scale(button, (100,100))
button2 = pygame.transform.scale(button, (120,120)) 

guessthenote = pygame.image.load(r"C:\Users\noobp\Documents\congressional-challenge\images\guessthenote.png")
guessthenote = pygame.transform.scale(guessthenote, (250,100))

settings = pygame.image.load(r"C:\Users\noobp\Documents\congressional-challenge\images\settingsbutton.png")
settings = pygame.transform.scale(settings, (50,50))
settings2 = pygame.transform.scale(settings, (60,60))

unselected = pygame.image.load(r"C:\Users\noobp\Documents\congressional-challenge\images\unchecked.png")
unselected = pygame.transform.scale(unselected, (25,25))
selected = pygame.image.load(r"C:\Users\noobp\Documents\congressional-challenge\images\checked.png")
selected = pygame.transform.scale(selected, (25,25))

modestates = ["guessnote","mainmenu"]
states = ["play_sound","waiting","validation","main","settings"]

currentstate = "main"

gamemode = "mainmenu"

timer = 0
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
confetti_particles = []
CONFETTI_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), ORANGE]

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


def play_note_random():
    note = random.choice(normalnotes + accidentals)
    sound = pygame.mixer.Sound(rf"Notes\{note}.mp3")
    sound.play()
    print("playing note")
    return note

clicked = False
mouse_pos = (0,0)
running = True
keysWHITE = []
keysBLACK = []
x = 50
for i in range(21):
    keysWHITE.append(Key(normalnotes[i], WHITE, i * 35 + 30, 300, font))
for i in range(15):
    keysBLACK.append(Key(accidentals[i], BLACK, x, 200, font))
    if accidentals[i][0] == "E" or accidentals[i][0] == "B":
        x += 35
    x += 35
playbutton = GameButton(350, 75, 125, 75, WHITE, font, button, button2, ORANGE, screen)
guessthenotebutton = GuessTheNoteButton(300, 200, 200, 100, WHITE, font, guessthenote, guessthenote, ORANGE, screen)
settingsbutton = SettingsButton(725, 25, 100, 100, WHITE, font, settings, settings2, ORANGE, screen)

allnotes = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
toggle_buttons = []

for note in allnotes:
    toggle_buttons.append(ToggleButton(600, 50 + allnotes.index(note) * 40, 25, 25, WHITE, font, unselected, selected, BLACK, screen, note))
    
    


while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                clicked = False

    mouse_pos = pygame.mouse.get_pos()       
            
    # 2. Update Game State
    
    # 3. Draw
    screen.fill(BEIGE)
    cooldown -= 1
    confetti_particles = [particle for particle in confetti_particles if particle.update()]


    if gamemode == "guessnote":

        settingsbutton.show(mouse_pos)
        

        if not currentstate == "settings":
            for key in keysWHITE:
                key.show(screen, clicked, mouse_pos, cooldown)
            for key in keysBLACK:
                key.show(screen, clicked, mouse_pos, cooldown)
        
            # time.sleep(2.0)

    
        if currentstate == "settings":
            if settingsbutton.clicked(clicked, mouse_pos):
                currentstate = "main"
            for button in toggle_buttons:
                button.show(mouse_pos)
                button.clicked(clicked, mouse_pos)
        elif currentstate == "main":
            if settingsbutton.clicked(clicked, mouse_pos):
                currentstate = "settings"
            playbutton.show(mouse_pos)
            if playbutton.clicked(clicked, mouse_pos):
                currentstate = "play_sound"
        elif currentstate == "play_sound":
            correct_note = play_note_random()  
            print(f"Correct note: {correct_note}")
            currentstate = "waiting"
        elif currentstate == "waiting":
            if settingsbutton.clicked(clicked, mouse_pos):
                currentstate = "settings"
            played = False
            note = None
            for key in keysBLACK:
                played, note, cooldown = key.playnote(clicked, mouse_pos, cooldown)
                if played:
                    timer = 0
                    currentstate = "validation"
                    break
            if not played:
                for key in keysWHITE:
                    played, note, cooldown = key.playnote(clicked, mouse_pos, cooldown)
                    if played:
                        timer = 0
                        currentstate = "validation"
                        break
        if currentstate == "validation":
            if settingsbutton.clicked(clicked, mouse_pos):
                currentstate = "settings"
            print(f"Played {note}")
            playbutton.validate_note(note, correct_note, screen, confetti_particles, CONFETTI_COLORS, WIDTH)
            timer += 1
            if timer > 60:
                currentstate = "main"

        for particle in confetti_particles:
            particle.show(screen)
    if gamemode == "mainmenu":
        guessthenotebutton.show(mouse_pos)
        if guessthenotebutton.clicked(clicked, mouse_pos):
            gamemode = "guessnote"
            currentstate = "main"
    screen.blit(image, (0,0))
    # Update the display
    pygame.display.flip()
    
    #to show the image
    
    # Cap the frame rate
    clock.tick(FPS)
    
    




