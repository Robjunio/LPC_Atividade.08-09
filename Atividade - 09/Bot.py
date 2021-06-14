import pygame
from Cube import *
from Snake import *
from utils import *


pygame.init()


class Bot(object):
    bot_body = []
    bot_turns = {}


    def __init__(self, color, pos, rows, width):
        self.color = color
        self.head = Cube(pos, rows=rows, width=width)
        self.bot_body.append(self.head)
        self.dirx = 0
        self.diry = 1
        self.rows = rows
        self.width = width

     
    def collision(pos0, pos1):
        return pos0[0] == pos1[0] and pos0[1] == pos1[1]


    def evade(self):
        self.dont = []
        a, b, c, d = 0, 0, 0, 0
        
        right_collision = (self.head.pos[0] + 1, self.head.pos[1])
        left_collision = (self.head.pos[0] - 1, self.head.pos[1])
        up_collision = (self.head.pos[0], self.head.pos[1] - 1)
        down_collision = (self.head.pos[0], self.head.pos[1] + 1)
        
        for i in range(1, len(self.bot_body)):
            if a == 0:
                if (collision(right_collision, self.bot_body[i])):
                    self.dont.append(RIGHT)
                    a += 1
            if b == 0:
                if (collision(left_collision, self.bot_body[i])):
                    self.dont.append(LEFT)
                    b += 1
            if c == 0:
                if (collision(up_collision, self.bot_body[i])):
                    self.dont.append(UP)
                    c += 1
            if d == 0:    
                if (collision(down_collision, self.bot_body[i])):
                    self.dont.append(DOWN)
                    d += 1
        return self.dont
        
    
    def move(self, apple_pos):
        dont = self.evade()
        if self.head.pos[0] != apple_pos[0]:
            if self.head.pos[0] < apple_pos[0]:
                if LEFT not in dont:
                    self.dirnx = -1
                    self.dirny = 0
                    self.bot_turns[self.head.pos[:]] = [self.dirnx, self.dirny]   
            else:
                if RIGHT not in dont:
                    self.dirnx = 1
                    self.dirny = 0
                    self.bot_turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
        elif self.head.pos[1] != apple_pos[1]:
            if self.head.pos[1] < apple_pos[1]:
                if UP not in dont:
                    self.dirnx = 0
                    self.dirny = -1
                    self.bot_turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            else:
                if DOWN not in dont:
                    self.dirnx = 0
                    self.dirny = 1
                    self.bot_turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.bot_body):
            p = c.pos[:]
            if p in self.bot_turns:
                turn = self.bot_turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.bot_body) - 1:
                    self.bot_turns.pop(p)
            else:
                if c.displacement_x_axis == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.displacement_x_axis == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.displacement_y_axis == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.displacement_y_axis == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.displacement_x_axis, c.displacement_y_axis)

    def add_body(self):
        tail = self.bot_body[-1]
        dx, dy = tail.displacement_x_axis, tail.displacement_y_axis

        if dx == 1 and dy == 0:
            self.bot_body.append(Cube((tail.pos[0] - 1, tail.pos[1]), rows=self.rows, width=self.width))
        elif dx == -1 and dy == 0:
            self.bot_body.append(Cube((tail.pos[0] + 1, tail.pos[1]), rows=self.rows, width=self.width))
        elif dx == 0 and dy == 1:
            self.bot_body.append(Cube((tail.pos[0], tail.pos[1] - 1), rows=self.rows, width=self.width))
        elif dx == 0 and dy == -1:
            self.bot_body.append(Cube((tail.pos[0], tail.pos[1] + 1), rows=self.rows, width=self.width))

        self.bot_body[-1].displacement_x_axis = dx
        self.bot_body[-1].displacement_y_axis = dy

    def reset(self, pos):
        self.bot_body = []
        self.head = Cube(pos)
        self.bot_body.append(self.head)
        self.bot_turns = {}
        self.dirnx = 0
        self.dirny = 1

    def draw(self, surface):
        for i, c in enumerate(self.bot_body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
