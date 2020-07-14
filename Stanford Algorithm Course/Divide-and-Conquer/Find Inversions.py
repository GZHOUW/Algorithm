def countInv(A):
    '''
    :param A: list of distinct integers
    :return: the number of inversions in A
    '''
    mid = len(A)//2
    left = A[:mid]
    right = A[mid:]
    if len(A) <= 1: # no inversions
        return 0
    else:
        # all left and right invs will eventually become split invs
        lInv = countInv(left)
        rInv = countInv(right)
        splitInv = countSplitInv(left, right, A)
        return lInv + rInv + splitInv


def countSplitInv(left,right,array):
    '''
    :param lSorted: sorted list with length n
    :param rSorted: sorted list with length n
    :return: the merge sorted version of lSorted and rSorted, the number of split inversions in lSorted and rSorted
    '''
    i = j = k = count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
            count = count + len(left) - i
        k = k + 1

    while i < len(left):
        array[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        array[k] = right[j]
        j = j + 1
        k = k + 1

    return count

text_file = open("nums.txt", "r")
lines = text_file.read().split('\n')
for i in range(len(lines)):
    lines[i]= int(lines[i])
a = countInv(lines)
print(a)
