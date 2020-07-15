'''
There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:
  Input: [1,0,2]
  Output: 5
  Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
  
Example 2:
  Input: [1,2,2]
  Output: 4
  Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
               The third child gets 1 candy because it satisfies the above two conditions.
'''

class Solution:
    def candy(self, ratings):
        candy = [1 for _ in ratings]
        
        # if a child has high rating than his LEFT neighbor, give him candies until he has 1 more than his LEFT neighbor
        # e.g. rating = [1,0,2], candy = [1,1,1] --> [1,1,2]
        for i in range(1, len(candy)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1
        
        # if a child has high rating than his RIGHT neighbor, either do nothing or give him candies until he has 1 more than his RIGHT neighbor
        # depending on which number is higher
        # candy = [1,1,2] --> [2,1,2]
        for j in range(len(candy)-2, -1, -1):
            if ratings[j] > ratings[j+1]:
                candy[j] = max(candy[j], candy[j+1] + 1)
                                                                  
        return sum(candy)
        
        
            
