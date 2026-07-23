import random
import pygame


class ConfettiParticle:
    def __init__(self, x, y, colors):
        self.x = x
        self.y = y
        self.size = random.randint(4, 8)
        self.color = random.choice(colors)
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-6, -1)
        self.life = random.randint(40, 70)

    def update(self):
        self.vy += 0.2
        self.x += self.vx
        self.y += self.vy
        self.life -= 1
        return self.life > 0

    def show(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


def spawn_confetti(x, y, amount, particles, colors):
    for _ in range(amount):
        particles.append(ConfettiParticle(x, y, colors))
