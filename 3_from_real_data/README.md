##  Transaction Generation with Manually Coded Agents: A More Useful Approach

###  Explanation
agent.py defines at each timestep what the probability of an agent taking an action is.
More complicated logic is within the agents this time around, 
but the program attempts to create agents that match the resulting data as much as possible.

###  To Use
```bash
python3 scheduler.py
```

###  Approach Flaws
- Transactions are not domain agnostic. If I wanted to model clothes shopping, I would need 
to do some legwork.

- Strange agents are likely to appear. Really unrealistic single agents. Even if you get good macro data, 
it does not guarantee good micro data.

- Even if I used reasonable probabilities that i derived from real 
data, at the end of the day, the agents don't have preferences. They dont change their jobs. 
They don't watch commercials, or buy new brands. They don't have children and start buying diapers. 
Essentially agent based data only works for patterns at the macro level.

##  Coming Up Next: A More Flexible Approach
- Replace all the internal agent logic with some more flexible knobs that are generated from 
the dataset. That is to say, not just the knob values are generated, but the available types of transactions 
and available periodicities are also generated. Consider multimodal distributions as well.




