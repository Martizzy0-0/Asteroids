import random

from circleshape import *
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
    
    def draw(self, screen: pygame.Surface):        
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20,50)
            
            asterotation_1 = self.velocity.rotate(rand_angle)
            asterotation_2 = self.velocity.rotate(-rand_angle)
            
            asteradius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid_1 = Asteroid(self.position.x, self.position.y, asteradius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, asteradius)
            
            asteroid_1.velocity *= 1.2