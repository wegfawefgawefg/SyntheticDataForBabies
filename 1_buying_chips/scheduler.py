import random
from pprint import pprint
import datetime
from dateutil.relativedelta import relativedelta

import pandas as pd
import numpy as np
from tqdm import tqdm

from agent import Agent

if __name__ == "__main__":
    NUM_AGENTS = 10

    START = datetime.datetime(2019, 7, 1)
    END = datetime.datetime(2019, 8, 1)
    DURATION = END - START
    NUM_HOURS = DURATION.days * 24

    agents = [Agent(id=i) for i in range(NUM_AGENTS)]
    datetimes = [START + datetime.timedelta(hours=x) for x in range(NUM_HOURS)]

    data = []
    for dt in tqdm(datetimes):
        random.shuffle(agents)
        for agent in agents:
            new_data = agent.step(dt)
            if new_data:
                data.append(new_data)

    df = pd.DataFrame(data, columns=["datetime", "id", "info", "amount"])
    print(df.head())

    #   save data to csv file 