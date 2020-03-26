'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

def findMedianSortedArrays(self, nums1, nums2):
    pInf = float('inf')
    nInf = -float('inf')
    len1 = len(nums1)
    len2 = len(nums2)
    if len1 > len2: # make sure nums1 is shorter
        nums1, nums2, len1, len2 = nums2, nums1, len2, len1
    if len1 == 0:
        return (nums2[(len2-1)//2] + nums2[len2//2])/2 # works for both even and odd

    size = len1 + len2
    # boundaries of cut1, contain possible cut1 values; later perform binary search within cut1L and cut1R
    cut1 = 0
    cut1L = 0
    cut1R = len1

    while cut1 <= len1:
        cut1 = (cut1R - cut1L) // 2 + cut1L # number of elements on the left of the cut
        # mid position between cut1L and cut1R
        cut2 = size // 2 - cut1 # ensures that left has same number of elements as right

        if cut1 == 0:
            L1 = nInf
        else:
            L1 = nums1[cut1 - 1] 

        if cut1 == len1:
            R1 = pInf
        else:
            R1 = nums1[cut1]

        if cut2 == 0:
            L2 = nInf
        else:
            L2 = nums2[cut2 - 1]

        if cut2 == len2:
            R2 = pInf
        else:
            R2 = nums2[cut2]

        if L1 > R2: # cut should move left
            cut1R = cut1 - 1 # right boundary is set to the element on the left of the cut
        elif L2 > R1: # cut should move right
            cut1L = cut1 + 1
        else: # L1 <= R2 and L2 <= R1 ---> correct cut
            if size % 2 == 0: # even
                return (max(L1, L2) + min(R1, R2)) / 2
            else: # odd
                return min(R1, R2)
                    
                    
''' JAVA Solution
public class MedianOfTwoSortedArrays {
    public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int MIN_VALUE = 0x80000000;
        int MAX_VALUE = 0x7fffffff;

        int N1 = nums1.length;
        int N2 = nums2.length;
        if (N1 > N2) {
            return findMedianSortedArrays(nums2, nums1);
        }

        if (N1 == 0)
            return ((double) nums2[(N2 - 1) / 2] + (double) nums2[N2 / 2]) / 2;
        int size = N1 + N2;
        int cutL = 0, cutR = N1;
        int cut1 = 0;
        int cut2;

        while (cut1 <= N1) {
            cut1 = (cutR - cutL) / 2 + cutL;
            cut2 = size / 2 - cut1;

            double L1 = (cut1 == 0) ? MIN_VALUE : nums1[cut1 - 1];
            double L2 = (cut2 == 0) ? MIN_VALUE : nums2[cut2 - 1];
            double R1 = (cut1 == N1) ? MAX_VALUE : nums1[cut1];
            double R2 = (cut2 == N2) ? MAX_VALUE : nums2[cut2];
            if (L1 > R2)
                cutR = cut1 - 1;
            else if (L2 > R1)
                cutL = cut1 + 1;
            else {// Otherwise, that's the right cut.
                if (size % 2 == 0) {
                    L1 = (L1 > L2 ? L1 : L2);
                    R1 = (R1 < R2 ? R1 : R2);
                    return (L1 + R1) / 2;
                }

                else {
                    R1 = (R1 < R2 ? R1 : R2);
                    return R1;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args){
        int[] b = new int[]{1,3,4,7,8,10,20};
        int[] a = new int[]{2,9,12,13};
        double m = findMedianSortedArrays(a, b);
        System.out.println(m);
    }
}


'''
