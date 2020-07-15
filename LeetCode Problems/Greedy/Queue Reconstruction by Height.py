'''
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.
 
Example
    Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

    Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

class Solution:
    def reconstructQueue(self, people):
        
        # sort the people in the order of descending h. If multiple people have same height, sort them in ascending k
        # i.e. [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]] --> [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        
        res = []
        for p in people:
            res.insert(p[1], p) # insert p at position p[1]
            '''
            Tallest people are inserted first, and they will not affect the position of shorter people
            because either h_cur < h_prev, or (h_cur=h_prev and k_cur>k_prev)
            不管在哪里添加多少个矮的，都不会使高的人的位置变得不正确
            [[7,0],[7,1]] ---> [[7,0],[6,1],[7,1]] or [[7,0],[7,1],[6,2]] or [[6,0],[7,0],[7,1]]
            '''
        return res
