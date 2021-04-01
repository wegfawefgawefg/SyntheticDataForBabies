import random
from pprint import pprint
import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd
import numpy as np
from tqdm import tqdm
from pprint import pprint

from agent import Agent
from buy import Buy, Item, When
from chance import FlatChance, HourChance

if __name__ == "__main__":
    NUM_AGENTS = 10

    START = datetime.datetime(2019, 7, 1)
    END = datetime.datetime(2019, 8, 1)
    DURATION = END - START
    NUM_HOURS = DURATION.days * 24

    buys = [
        Buy(item=Item(name="netflix_subscription", price=11.0),
            when=When(),
            chance=FlatChance(0.01)),
        #   buying gas in the morning
        Buy(item=Item(name="gas", price=20.0, std=0.1),
            when=When(),
            chance=HourChance(hour=6, chance_scale=0.1)),
        #   buying gas in the evening
        Buy(item=Item(name="gas", price=20.0, std=0.1),
            when=When(),
            chance=HourChance(hour=18, chance_scale=0.1)),
        #   buying chips at the gas station after work
        Buy(item=Item(name="chips", price=3.0, std=0.05),
            when=When(),
            chance=HourChance(hour=18, chance_scale=0.1)),
    ]

    agents = [Agent(id=i, buys=buys) for i in range(NUM_AGENTS)]
    datetimes = [START + datetime.timedelta(hours=x) for x in range(NUM_HOURS)]

    data = []
    for dt in tqdm(datetimes):
        random.shuffle(agents)
        for agent in agents:
            new_datas = agent.step(dt)
            for new_data in new_datas:
                data.append(new_data)

    df = pd.DataFrame(data, columns=["datetime", "id", "info", "amount"])
    print(df.head(50))

    #   save data to csv file 