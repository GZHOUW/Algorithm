'''
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
  Input: n = 3, k = 3
  Output: "213"

Example 2:
  Input: n = 4, k = 9
  Output: "2314"
'''

def getPermutation(n, k):
    numbers = [i for i in range(1, n+1)]
    permutation = ''
    k -= 1 # change k into index value instead of 'k th' permutation
    while n > 0:
        # there are (n-1)! perms that start with 1, (n-1)! that start with 2, ect.

        # Find out which (n-1)! segment k is in --> store in index
        index, k = divmod(k, math.factorial(n-1)) # quotient and remainder

        # get the number that corresponds to index
        permutation += str(numbers[index])

        # remove handled number
        numbers.remove(numbers[index])

        # repeat with new number list and new n&k values
        n -= 1

    return permutation
