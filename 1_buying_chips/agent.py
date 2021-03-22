import random

import numpy as np

class Agent:
    def __init__(self, id):
        self.id = id
        self.buy_chips = 0.001

    def step(self, dt):
        if random.random() <= self.buy_chips:
            return (dt, self.id, "chips", 2.45)
        return None