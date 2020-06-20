
def sortCountInv(A):
    '''
    :param A: list of distinct integers
    :return: the sorted version of A,   the number of inversions in A
    '''

    if len(A) == 0 or len(A) == 1: # no inversions
        return A, 0
    else:
        # all left and right invs will eventually become split invs
        lSorted, lInv = sortCountInv(A[:len(A)//2])
        rSorted, rInv = sortCountInv(A[len(A)//2:])
        allSorted, splitInv = mergeCountSplitInv(lSorted, rSorted)

        invCount = lInv + rInv + splitInv
        return allSorted, invCount


def mergeCountSplitInv(lSorted, rSorted):
    '''
    :param lSorted: sorted list with length n
    :param rSorted: sorted list with length n
    :return: the merge sorted version of lSorted and rSorted, the number of split inversions in lSorted and rSorted
    '''
    splitInv = 0
    allSorted = [None] * (len(lSorted)+len(rSorted))
    l = 0
    r = 0
    idx = 0
    while l < len(lSorted) and r < len(rSorted):
        if lSorted[l] < rSorted[r]:
            allSorted[idx] = lSorted[l]
            l += 1
        else:
            allSorted[idx] = rSorted[r]
            if r <= l: # if the second half's element is added to allSorted before first half's, a split inv is found
                splitInv += 1
            r += 1
        idx += 1

    while l < len(lSorted):
        allSorted[idx] = lSorted[l]
        l += 1
        idx += 1

    while r < len(rSorted):
        allSorted[idx] = rSorted[r]
        r += 1
        idx += 1
    return allSorted, splitInv


print(sortCountInv([1,2,6,3,4,5,7]))