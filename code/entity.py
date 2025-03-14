#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name:str, position:tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png') # load the png image in the asset folder
        self.rect = self.surf.get_rect(left=position[0], right=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass
