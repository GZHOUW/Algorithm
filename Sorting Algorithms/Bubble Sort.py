def BubbleSort(L):
    if len(L) <= 1: # must be sorted
        return L
    for i in range(len(L)):  # every iteration of outer loop puts the next smallest number in place
        left = len(L) - 2
        right = len(L) - 1
        while left >= i: # 0:i elements are already sorted, no need to check
            if L[left] > L[right]:  # incorrect pair
                L[left], L[right] = L[right], L[left]  # swap
            left -= 1
            right -= 1
    return L


print(BubbleSort([5,2,9,4,7,6,1,3,8]))