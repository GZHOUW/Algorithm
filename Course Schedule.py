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
        visited = [0 for _ in range(numCourses)]  # 0:not visited 1: visited 2: being visited
        graph = [[] for _ in range(numCourses)]  # [the nodes that cur node points to]

        for [cur, curPointTo] in prerequisites:
            graph[cur].append(curPointTo)

        for node in range(numCourses):
            if not self.dfs(graph, visited, node):
                return False
        return True

    def dfs(self, graph, visited, node):

        if visited[node] == 2:  # if cur node is  being visited, a circle is completed, return False
            return False

        if visited[node] == 1:  # if cur is visted, the chain reached an end without completing a circle, return True
            return True

        visited[node] = 2  # mark as being visited; being visited means still in the current dfs tree, or the 'circle'

        for neighbor in graph[node]:
            if not self.dfs(graph, visited, neighbor):  # visit all the neighbours
                return False

        visited[node] = 1  # after visiting all neighbors, mark cur node as visited
        return True
