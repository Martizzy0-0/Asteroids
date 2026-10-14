import pygame
from circleshape import *
from constants import PLAYER_RADIUS, LINE_WIDTH

class Player(CircleShape):
    rotation = 0
    
    def __init__(self, x, y, PLAYER_RADIUS):
        super().__init__(x, y, PLAYER_RADIUS)
        
    def draw(self, screen) -> None:
        __polygons = self.triangle()
        pygame.draw.polygon(screen, "white", __polygons, width=LINE_WIDTH)
        
    
    # draw player shape
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]