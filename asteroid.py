from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        clockwise = self.position.rotate(angle)
        counterclockwise = self.position.rotate(-angle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        one = Asteroid(self.position.x, self.position.y, radius)
        two = Asteroid(self.position.x, self.position.y, radius)
        one.velocity = clockwise * 1.2
        two.velocity = counterclockwise * 1.2