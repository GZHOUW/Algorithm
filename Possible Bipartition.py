'''
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group. 
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
'''

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        # create a map where nodes link to each other by dislike relationship
        node_map = {key: [] for key in range(1, N+1)}  # {node:neighbors}
        for link in dislikes:
            node_map[link[0]].append(link[1])
            node_map[link[1]].append(link[0])
        
        '''
        UNGROUPED = 0
        GROUP_A = 1
        GROUP_B = -1
        '''
        group_list = [ 0 for _ in range(N+1) ]  # group_list[idx] stores the group for which node idx is assigned to. All nodes are initially ungrouped, idx=0 is dummy
        
        for node in range(1, N+1):
            if group_list[node] == 0:
                isBipart = self.dfs(node, node_map, 1, group_list)
                if not isBipart:
                    return False
        return True        
        
    def dfs(self, node, node_map, group, group_list):
        group_list[node] = group  # Assign the current node to a group, this group must be different from previous node
        
        for neighbor in node_map[node]:
            if group_list[neighbor] == group:  # two of same groups are linked, False
                return False
            
            if  group_list[neighbor] == 0:
                isBipart = self.dfs(neighbor, node_map, -group, group_list)
                if not isBipart:
                    return False
                
        return True
