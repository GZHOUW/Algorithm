'''
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
  Input: 
  n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
  src = 0, dst = 2, k = 1
  Output: 200
  Explanation: 
  The cheapest price from city 0 to city 2 with at most 1 stop costs 200.
'''

def findCheapestPrice(self, n, flights, src, dst, K):
    # ex: flights=[[0,1,100],[1,2,100],[0,2,500]]
    graph = collections.defaultdict(list)  # {from:[price, to]}
    q = collections.deque()  # [(city, n_stops, price)] where n_stops and price are needed to get to city
    minCost = float('inf')  # when price exceed minCost, stop searching

    for u, v, price in flights:
        graph[u].append((price, v))
    # graph = {0: [(100, 1), (500, 2)], 1: [(100, 2)]}

    q.append((src, 0, 0))  # it takes 0 stops and 0 cost to get to src

    while q:
        curCity, curStops, curCost = q.popleft()
        if curCity == dst:
            minCost = min(minCost, curCost)
            continue

        if curStops <= K and curCost <= minCost:
            for nextCost, nextCity in graph[curCity]:
                q.append((nextCity, curStops + 1, curCost + nextCost))

    if minCost == float('inf'):
        return -1 
    return minCost
