def SelectionSort(L):
    startPos = 0
    while startPos < len(L):
        for i in range(startPos, len(L)):
            if L[i] == min(L[startPos:]):
                L[i], L[startPos] = L[startPos], L[i]
        startPos += 1
    return L


print(SelectionSort([5,2,9,4,7,6,1,3,8]))