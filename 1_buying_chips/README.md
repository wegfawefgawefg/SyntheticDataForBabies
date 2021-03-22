##  Transaction Generation with Manually Coded Agents: A Naive Approach

###  Explanation
agent.py defines at each timestep what the probability of an agent taking an action is.

###  To Use
'''bash
python3 scheduler.py
'''

###  Data Flaws
- As you can see, the agents buy only one type of chips.
- The price does not vary.
- The purchase is always on the hour.
- There is no pattern in when they buy chips, meaning an agent is just as likely to buy chips at 1AM, as 3PM.
- Days of the week are not considered.
- Holidays are not considered
- Agents do not have a true schedule

###  Approach Flaws
- Oversimplification of real behaviour.

###  Potential Additions
- add hour offsets, from normal distributions
- add cooldowns after purchases
- add agent account amounts
- consider agent paycheck times
- track agents working hours, and days

Each of these additions should take 5-10 minutes to add, 
and they build on the complexity of the resulting data.

##  Coming Up Next: The Elbow Grease Approach
- MORE ADDITIONS
