'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. 
All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.

Example 1:
  Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
  Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
  Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
  Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
  Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
               But it is larger in lexical order.
'''

class Solution:
    def findItinerary(self, tickets):
        # a dict where key is a departure airport, element is a list of airports where 
        # the flights from the departure airport lands on
        self.airportDict = collections.defaultdict(list) 
        for depar, desti in sorted(tickets)[::-1]:
            self.airportDict[depar].append(desti),
            
        self.route = [] # contains airports in the order of visit
        self.visit('JFK')
        return self.route[::-1]
    
    def visit(self, airport):
        while self.airportDict[airport]:
            self.visit(self.airportDict[airport].pop()) # visit as many airports as possible
        self.route.append(airport) # and then append airports in backwards order
        '''
        e.g. {SFO:[ATL], JFK:[SFO, ATL], ATL:[SFO, JFK]}
        visit(JFK) --> pop(ATL) --> {SFO:[ATL], JFK:[SFO], ATL:[SFO, JFK]}
        visit(ATL) --> pop(JFK) --> {SFO:[ATL], JFK:[SFO], ATL:[SFO]}
        visit(JFK) --> pop(SFO) --> {SFO:[ATL], JFK:[], ATL:[SFO]}
        visit(SFO) --> pop(ATL) --> {SFO:[], JFK:[], ATL:[SFO]}
        visit(ATL) --> pop(SFO) --> {SFO:[], JFK:[], ATL:[]}
        visit(SFO) --> dict is empty --> start append backwards --> [SFO,ATL,SFO,JFK,ATL,JFK]
        '''
