class Solution:
    def nthUglyNumber(self, n):
        ugly = [1] # stores ugly numbers in ascending order
        
        # pointers that point at the next numbers to be chosen as candidates to multiply by 2,3,5
        idx2 = 0 
        idx3 = 0
        idx5 = 0
        
        while len(ugly) < n:
            # 3 candidates, choose the smallest
            num2 = 2*ugly[idx2] # num2 might be same as num3 or num5
            num3 = 3*ugly[idx3]
            num5 = 5*ugly[idx5]
            nextUglyNum = min(num2, num3, num5)
            ugly.append(nextUglyNum)
            if nextUglyNum == num2: # the number at current idx2 is already used, move it to next number
                idx2 += 1
            if nextUglyNum == num3:
                idx3 += 1
            if nextUglyNum == num5:
                idx5 += 1
            
        return ugly[-1]
