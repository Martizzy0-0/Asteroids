from circleshape import *
from constants import LINE_WIDTH

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.center = pygame.Vector2(self.x, self.y)
    
    def draw(self, screen: pygame.Surface):        
        pygame.draw.circle(screen, "white", self.center, self.radius, LINE_WIDTH)
    
    def update(self, dt: float):
        self.center += self.velocity * dt