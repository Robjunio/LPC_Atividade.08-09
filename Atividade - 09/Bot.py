import pygame
from Cube import *
from Snake import *
pygame.init()


class Bot(object):
    bot_body = []
    bot_turns = {}


    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.bot_body.append(self.head)
        self.dirx = 0
        self.diry = 1


    # Uma função para facilitar a detecção de colisão       
    def collision(pos0, pos1):
        return pos0[0] == pos1[0] and pos0[1] == pos1[1]


    # A seguinte função tem como objetivo ver se o bot poderá ou não fazer os
    # movimento de U, D, L e R. Se não poder eles serão colocados em uma lista
    # a qual será retornada na função de movimento, e lá será verificado se o
    # movimento que será feito é possivel ou não.
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
                    self.dont.append(R)
                    a += 1
            if b == 0:
                if (collision(left_collision, self.bot_body[i])):
                    self.dont.append(L)
                    b += 1
            if c == 0:
                if (collision(up_collision, self.bot_body[i])):
                    self.dont.append(U)
                    c += 1
            if d == 0:    
                if (collision(down_collision, self.bot_body[i])):
                    self.dont.append(D)
                    d += 1
        return self.dont
        
    
    def move(self, apple_pos, movement):
        dont = evade()
        if self.head.pos[0] != apple_pos[0]:
            if self.head.pos[0] < apple_pos[0]:
                if L not in dont:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]   
            else:
                if R not in dont:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
                    
        elif self.head.pos[1] != apple_pos[1]:
            if self.head.pos[1] < apple_pos[1]:
                if U not in dont:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]
            else:
                if D not in dont:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body) - 1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows - 1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:
                    c.pos = (0, c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:
                    c.pos = (c.pos[0], 0)
                elif c.dirny == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows - 1)
                else:
                    c.move(c.dirnx, c.dirny)

    def add_body(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        if dx == 1 and dy == 0:
            self.body.append(Cube((tail.pos[0] - 1, tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(Cube((tail.pos[0] + 1, tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] - 1)))
        elif dx == 0 and dy == -1:
            self.body.append(Cube((tail.pos[0], tail.pos[1] + 1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def reset(self, pos):
        self.body = []
        self.head = Cube(pos)
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.draw(surface, True)
            else:
                c.draw(surface)
