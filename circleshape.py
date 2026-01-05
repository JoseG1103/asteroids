import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other):
        # distance between centers is <= sum of the radii -> collision
        sum_of_radii = self.radius + other.radius
        distance_centers = self.position.distance_to(other.position)
        return distance_centers <= sum_of_radii

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

