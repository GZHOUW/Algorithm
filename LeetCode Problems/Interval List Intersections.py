'''
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
'''

def intervalIntersection(A, B):
    a = 0  # idx pointers that point at invervals in a and b
    b = 0
    res = []

    while a < len(A) and b < len(B):
        if A[a][1] < B[b][0]:  # no interval
            a += 1
        elif B[b][1] < A[a][0]:  # no interval
            b += 1
        elif A[a][0] <= B[b][0]:
            if A[a][1] <= B[b][1]:  # A=[1,3] B=[2,4]
                res.append([B[b][0], A[a][1]])
                a += 1
            else:  # A = [1,5] B=[2,4]
                res.append([B[b][0], B[b][1]])
                b += 1
        else: # A[a][0] > B[b][0]
            if A[a][1] <= B[b][1]:  # B=[1,3] A=[2,4]
                res.append([A[a][0], A[a][1]])
                a += 1
            else:
                res.append([A[a][0], B[b][1]])
                b += 1
    return res
