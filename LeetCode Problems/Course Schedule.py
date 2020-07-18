'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''

class Solution:
    def canFinish(self, numCourses, prerequisites):
        self.state = [0 for _ in range(numCourses)] # 0:not visited 1: visited 2: being visited (current tree)
        
        self.graph = [[] for _ in range(numCourses)] # graph[i] denotes the list of prereqs of course i
        for [course, prereq] in prerequisites: 
            self.graph[course].append(prereq) # [[1,0],[0,2],[2,3],[3,4],[4,2]] --> [[2],[0],[3],[4],[2]]
        
        for course in range(numCourses): 
            if not self.dfs(course):
                return False
        return True
        
    def dfs(self, node):
        # start from a node and look for cycles, i.e. [0,1], [1,2], [2,0]
        if self.state[node] == 2: # if cur node is marked as being visited, then a cycle is found.
            return False
        
        if self.state[node] == 1: # if cur is visted, it (and its tree) is proven to be valid, return true
            return True
       
        self.state[node] = 2  # mark as being visited, means still in the current dfs tree, or the 'circle' that is not yet completed
        
        for neighbour in self.graph[node]:
            if not self.dfs(neighbour): # visit all the neighbours
                return False
            
        # At this point, all neighbours of cur node are visites and they are all valid
        self.state[node] = 1  # mark all nodes in cur tree as visited and return True because they are valid
        return True
