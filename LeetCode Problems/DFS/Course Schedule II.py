'''
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:
    Input: 2, [[1,0]] 
    Output: [0,1]
    Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
                 course 0. So the correct course order is [0,1] .
Example 2:
    Input: 4, [[1,0],[2,0],[3,1],[3,2]]
    Output: [0,1,2,3] or [0,2,1,3]
    Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
                 courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
                 So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
'''

class Solution:
    def findOrder(self, numCourses, prerequisites):
        self.order = []
        self.canFinsh = True
        self.state = [0 for _ in range(numCourses)] # 0:not visited 1: visited 2: being visited (current tree)
        self.graph = [[] for _ in range(numCourses)] # graph[i] denotes the list of prereqs of course i
        for [course, prereq] in prerequisites: 
            self.graph[course].append(prereq) # [[1,0],[0,2],[2,3],[3,4],[4,2]] --> [[2],[0],[3],[4],[2]]
        
        for course in range(numCourses): 
            self.dfs(course)
            
        if self.canFinsh:
            return self.order
        else:
            return []
        
    def dfs(self, node):
        
        if self.state[node] == 2:
            self.canFinsh = False
            return
        
        if self.state[node] == 1: 
            return # avoid duplicates
       
        self.state[node] = 2
        
        for neighbour in self.graph[node]:
            self.dfs(neighbour)
            
        self.order.append(node)
        self.state[node] = 1  
