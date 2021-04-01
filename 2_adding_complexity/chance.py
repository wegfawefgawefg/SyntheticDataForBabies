from abc import ABC, abstractmethod
import datetime 
import random

from scipy import stats
from utilities import circular_distance

class Chance:
    @abstractmethod
    def __init__(self):
        ''' whatever chance paramters are needed to make the chance '''
        pass

    @abstractmethod
    def __call__(self, dt: datetime) -> bool:
        ''' do a chance roll, return if you passed the check '''
        pass    

class FlatChance(Chance):
    def __init__(self, chance):
        self.chance = chance

    def __call__(self, dt):
        if random.random() <= self.chance:
            return True
        else:
            return False

class HourChance(Chance):
    NUM_HOURS = 24

    def __init__(self, hour, chance_scale=1.0, std=1.0, minimum=0.0):
        self.hour = hour
        self.chance_scale = chance_scale
        self.std = std
        self.minimum = minimum

    def __call__(self, dt):
        dist = circular_distance(HourChance.NUM_HOURS, self.hour, dt.hour)
        prob = self.chance_scale * stats.norm.pdf(dist, loc=0.0, scale=self.std)
        prob = max(prob, self.minimum)
        if random.random() <= prob:
            return True
        else:
            return False

if __name__ == "__main__":
    import math
    import matplotlib.pyplot as plt

    import numpy as np
    
    hchance = HourChance(1.0, 12, 0.1)
    dt = datetime.datetime(2021, 7, 6, 12)

    ys = []
    for i in range(24):
        dt = datetime.datetime(2021, 7, 6, i)
        y = hchance(dt) 
        ys.append(y)

    plt.plot(ys)
    plt.show()