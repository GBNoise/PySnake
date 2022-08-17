import pygame


class Hud:
    def __init__(self, width, height):
        self.surface = pygame.Surface((width, 200))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect(topright=(width, height))
        self.score = 0
        self.font = pygame.font.Font(pygame.font.get_default_font(),20)
        self.text_surface = self.font.render(f'Score is: {self.score} ',True, (0,0,0))
        self.surface.blit(self.text_surface, dest=(0,0))

    def update_score(self):
        self.text_surface = self.font.render(f'Score is: {self.score}', True, (0,0,0))
        self.surface.fill((255,255,255))
        self.surface.blit(self.text_surface, dest=(0,0))