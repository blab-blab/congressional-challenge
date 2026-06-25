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

notes = ["C","D","E","F","G","A","B"]



pygame.mixer.init()

c3 = pygame.mixer.Sound(r"Notes\C3.mp3")

c3.play()
time.sleep(2.0)