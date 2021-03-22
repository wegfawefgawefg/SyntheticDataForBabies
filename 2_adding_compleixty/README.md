##  Transaction Generation with Manually Coded Agents: A Man Hours Approach

###  Explanation
agent.py defines at each timestep what the probability of an agent taking an action is.
More complicated logic is within the agents this time around.

###  To Use
'''bash
python3 scheduler.py
'''

###  Approach Flaws
- The context of the data needs to be understood to be coded up as behaviour. 
This makes the complexity of the agents low, unless you spend a lot of time working on them. 
If you have a new domain you want to apply this strategy to, you are back at square one. 

- Pathalogical interactions between the agent decision logic is more and more likely as more 
knobs are added. These will not show up in the top down graphs, but some really weird agents could appear.

- Getting the resulting data to match real data transactions is difficult but not impossible

##  Coming Up Next: From Real Data
- Generating agent properties based on distribution matching via BOGO annealing (lol)


