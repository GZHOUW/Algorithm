'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
'''
def maximumProduct(nums):
      # find the three max numbers and two minimum numbers
      max1,max2,max3,min1,min2 = float('-Inf'),float('-Inf'),float('-Inf'),float('Inf'),float('Inf')
      for num in nums:
          if num >= max1:
              max3,max2,max1 = max2,max1,num
          elif num >= max2:
              max3,max2 = max2,num
          elif num > max3:
              max3 = num
          if num <= min1:
              min2,min1 = min1,num
          elif num < min2:
              min2 = num
      return max(max1*max2*max3, min1*min2*max1)
      '''
      EX1: [-10, -9, -2, -1, 3] ---> max1*max2*max3 = 6, min1*min2*max1 = 270
      EX2: [-10, -9,  1,  2, 3] ---> max1*max2*max3 = 6, min1*min2*max1 = 270
      EX3: [-10,  0,  1,  2, 3] ---> max1*max2*max3 = 6, min1*min2*max1 = 0
      EX4: [-10, -9, -3, -2,-1] ---> max1*max2*max3 = -6, min1*min2*max1 = -90

      '''
