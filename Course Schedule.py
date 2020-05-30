class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0 for _ in range(numCourses)] # 0:not visited 1: visited 2: being visited
        graph = [[] for _ in range(numCourses)] # [the nodes that cur node points to]

        for [cur, curPointTo] in prerequisites:
            graph[cur].append(curPointTo)

        for node in range(numCourses):
            if not self.dfs(graph, visited, node):
                return False
        return True
        
    def dfs(self, graph, visited, node):
        
        if visited[node] == 2: # if cur node is marked as being visited, then a cycle is found
            return False
        
        if visited[node] == 1: # if cur is visted, do not visit again
            return True
       
        visited[node] = 2  # mark as being visited--- being visited means still in the current dfs tree, or the 'circle' that is being completed
        
        for j in graph[node]:
            if not self.dfs(graph, visited, j): # visit all the neighbours
                return False
        
        visited[node] = 1  # after visiting all neighbours, mark visited
        return True
