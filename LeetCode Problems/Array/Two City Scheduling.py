'''
There are 2N people a company is planning to interview. 
The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110

Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
'''

def twoCitySchedCost(costs):
    totalCost = 0
    costDiff = [] # [cost B - cost A] --> how bad is the decision of going to A

    for idx, cost in enumerate(costs):
        costDiff.append((cost[1]-cost[0], idx))

    costDiff.sort() # large cost diff means decision to A is good, small is bad

    for i in range(len(costDiff)):
        idx = costDiff[i][1]
        if i < len(costDiff) / 2:  # first half goes to B
            totalCost += costs[idx][1]
        else:  # second half goes to A
            totalCost += costs[idx][0]

    return totalCost
