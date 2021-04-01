import random
import numpy as np

class Item:
    def __init__(self, name, price, std=0.0):
        self.name = name
        self.price = price
        self.std = std

    def get_price(self):
        return self.price +\
            self.price * np.random.normal(loc=0, scale=self.std)

class When:
    '''
        for now, time conditions do not exist, 
        inclusions or exclusions
    '''
    def __init__(self, include=None, exclude=None):
        self.include = include
        self.exclude = exclude

    def __call__(self, dt):
        return True

class Buy:
    def __init__(self, item, when, chance):
        self.item = item
        self.when = when
        self.chance = chance

    def chance_pass(self, dt):
        if self.when(dt):
            if self.chance(dt):
                return True
        return False

    def get_one(self, dt):
        return self.item.name, self.item.get_price()
        