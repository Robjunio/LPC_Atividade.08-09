import pygame
from utils import *


class Cube:

    def __init__(self, position, rows, width, color=RED):
        self.pos = position
        self.rows = rows
        self.width = width
        self.displacement_x_axis = 1
        self.displacement_y_axis = 0
        self.color = color

    def move(self, displacement_x_axis, displacement_y_axis):
        self.displacement_x_axis = displacement_x_axis
        self.displacement_y_axis = displacement_y_axis
        self.pos = (self.pos[0] + self.displacement_x_axis, self.pos[1] + self.displacement_y_axis)

    def draw(self, surface, has_eyes=False):
        dis = self.width // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2))
        if has_eyes:
            centre = dis // 2
            radius = 3
            left_eye = (i * dis + centre - radius, j * dis + 8)
            right_eye = (i * dis + dis - radius * 2, j * dis + 8)
            pygame.draw.circle(surface, BLACK, left_eye, radius)
            pygame.draw.circle(surface, BLACK, right_eye, radius)
