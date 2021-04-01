import random

import numpy as np

class Agent:
    def __init__(self, id, buys):
        self.id = id
        self.buys = buys

    def step(self, dt):
        ''' goes through possible buys
                does a chance roll, and makes a purchase if it passes '''
        purchases = []
        for buy in self.buys:
            if buy.chance_pass(dt):
                name, price = buy.get_one(dt)
                record = (dt, self.id, name, price)
                purchases.append(record)
        return purchases