'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
'''

class Solution():
    def kClosest(self, points, K):
        self.quickSort(points, 0, len(points)-1)
        return points[:K]
    
    def quickSort(self, points, start, end):
        if start < end:
            partIdx = self.partition(points, start, end) # get the pivot and place it correctly
            self.quickSort(points, start, partIdx-1) # recursively sort the sublist on the left of pivot
            self.quickSort(points, partIdx+1, end) # recursively sort the sublist on the right of pivot
        else:
            return

    def partition(self, points, start, end):
        pivot = end
        pivot_dist = points[pivot][0] ** 2 + points[pivot][1] ** 2
        partIdx = start
        # Place all elements that are smaller than pivot at the left of points
        # Then, the RIGHTMOST number that is smaller than pivot is the partIdx
        for i in range(start, end):
            i_dist = points[i][0]**2 + points[i][1]**2

            if i_dist <= pivot_dist:
                points[i], points[partIdx] = points[partIdx], points[i]
                partIdx += 1

        # place pivot at partIdx, which is the correctly sorted position of pivot
        points[pivot], points[partIdx] = points[partIdx], points[pivot]
        return partIdx
