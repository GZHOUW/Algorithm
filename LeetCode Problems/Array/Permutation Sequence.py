'''
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
  Input: n = 3, k = 3
  Output: "213"

Example 2:
  Input: n = 4, k = 9
  Output: "2314"
'''

class Solution:
    def getPermutation(self, n, k):
        '''
        Demo: n=3, k=5 --> nums = [1,2,3]
        perms = [1,2,3], [1,3,2], [2,1,3], [2,3,1],   [3,1,2],   [3,2,1]
                                                     k=5->4(idx)
        The first 2 (=(n-1)!) perms start with 1, the second 2 perms start with 2, ect
        idx = 4 // 2 = 2 --> third (n-1)! perms --> [3,1,2] or [3,2,1] --> start with 3 --> append 3 to res
        
        '''
        nums = [i for i in range(1, n+1)]
        res = ''
        k -= 1 # change k into index value instead of 'k th' permutation
        while n > 0:
            # there are (n-1)! perms that start with 1, (n-1)! that start with 2, ect.

            # Find out which (n-1)! segment k is in --> store in index
            idx = k // math.factorial(n-1)
            k = k % math.factorial(n-1)

            # get the number that corresponds to index
            res += str(nums[idx])

            # remove handled number
            nums.remove(nums[idx])

            # repeat with new number list and new n&k values
            n -= 1

        return res
