def InsertionSort(L):
    separation = 0  # everything at this index and before is sorted
    while separation < len(L)-1:
        temp = L[separation + 1]
        left = 0
        right = separation
        while left <= right:
            mid = (right - left)//2 + left
            if L[mid] < temp:
                left = mid + 1
            else:
                right = mid - 1
        for i in range(separation, right, -1):
            L[i+1] = L[i]
        L[right + 1] = temp
        separation += 1
    return L


print(InsertionSort([5,2,9,4,7,6,1,3,8]))