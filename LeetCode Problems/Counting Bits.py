'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Space complexity should be O(n).

Example 1:
  Input: 2
  Output: [0,1,1]

Example 2:
  Input: 5
  Output: [0,1,1,2,1,2]
'''

def countBits(num):
    '''
    Demo: 
    0
    0 1
    0 1 1 2
    0 1 1 2 1 2 2 3
    '''
    res = [0]
    while len(res)<=num:
        len_i = len(res)
        # copy all existing element in res, add one to each, and append to the end
        for i in range(len_i):  # cannot use for nBit in res because len keep changing
            res.append(res[i] + 1)
    return res[:num+1] # one more than num because of 0
