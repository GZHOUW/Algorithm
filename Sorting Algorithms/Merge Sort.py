def MergeSort(L):
    if len(L) > 1:
        mid = len(L) // 2  # Finding the mid of the array
        left = L[:mid]  # Dividing the array elements
        right = L[mid:]  # into 2 halves

        MergeSort(left)  # Sorting the first half
        MergeSort(right)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                L[k] = left[i]
                i += 1
            else:
                L[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            L[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            L[k] = right[j]
            j += 1
            k += 1
L = [5,2,9,4,7,6,1,3,8]
MergeSort(L)
print(L)