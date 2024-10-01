
'''
Define the Recurrence Relation:

The recurrence relation for the Stirling numbers of the second kind is: [ S(n, k) = k \\cdot S(n-1, k) + S(n-1, k-1) ]

We need to modify this to account for the pairs of twins.
we can take S(n,k) and minus the S(n-1,k) for 1 pair of twins and S(n,k) - m * s(n-1,k) for m pairs of twins.

Bases Cases:
Case 1: if n == 0 and k == 0:
This case returns 1 because there is exactly one way to partition an empty set (0 elements) into 0 non-empty subsets, which is the empty partition.

Case 2: if n == 0 or k == 0:
This case returns 0 because:
If n == 0 and k != 0, there are no ways to partition 0 elements into a positive number of non-empty subsets.
If k == 0 and n != 0, there are no ways to partition a positive number of elements into 0 non-empty subsets.

Function student_grouping(n, m, k):
This function calls stirling_second_kind a few times, but the dominant factor is still the time complexity of stirling_second_kind.
Hence the time complexity is O(n * k) for each test case.
The additional operations (printing and basic arithmetic) are negligible in comparison

'''
import sys

def stirling_second_kind(n, k, memo=None):
    if memo is None:
        memo = {}
    
    # Base cases
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    
    # Check if the value is already computed
    if (n, k) in memo:
        return memo[(n, k)]
    
   
    memo[(n, k)] = k * stirling_second_kind(n - 1, k, memo) + stirling_second_kind(n - 1, k - 1, memo)
    return memo[(n, k)]

def student_grouping(n, m, k):
    if m < 0:
        print("Impossible")
    elif m > 0:
        print(stirling_second_kind(n, k) - (m * stirling_second_kind(n - 1, k)))
    else:
        print(stirling_second_kind(n, k))

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m, k = a[0], a[1], a[2]
    student_grouping(n, m, k)


'''
Number of ways to partition 4 elements into 3 non-empty groups: 6
[[1, 4], [2], [3]]
[[1], [2, 4], [3]]
[[1], [2], [3, 4]]
[[1, 3], [2], [4]]
[[1], [2, 3], [4]]
[[1, 2], [3], [4]]

Number of ways to partition 5 elements into 3 non-empty groups: 25
[[1, 4, 5], [2], [3]]
[[1, 4], [2, 5], [3]]
[[1, 4], [2], [3, 5]]
[[1, 5], [2, 4], [3]]
[[1], [2, 4, 5], [3]]
[[1], [2, 4], [3, 5]]
[[1, 5], [2], [3, 4]]
[[1], [2, 5], [3, 4]]
[[1], [2], [3, 4, 5]]
[[1, 3, 5], [2], [4]]
[[1, 3], [2, 5], [4]]
[[1, 3], [2], [4, 5]]
[[1, 5], [2, 3], [4]]
[[1], [2, 3, 5], [4]]
[[1], [2, 3], [4, 5]]
[[1, 2, 5], [3], [4]]
[[1, 2], [3, 5], [4]]
[[1, 2], [3], [4, 5]]
[[1, 3, 4], [2], [5]]
[[1, 3], [2, 4], [5]]
[[1, 4], [2, 3], [5]]
[[1], [2, 3, 4], [5]]
[[1, 2, 4], [3], [5]]
[[1, 2], [3, 4], [5]]
[[1, 2, 3], [4], [5]]

Number of ways to partition 6 elements into 4 non-empty groups: 65
[[1, 5, 6], [2], [3], [4]]
[[1, 5], [2, 6], [3], [4]]
[[1, 5], [2], [3, 6], [4]]
[[1, 5], [2], [3], [4, 6]]
[[1, 6], [2, 5], [3], [4]]
[[1], [2, 5, 6], [3], [4]]
[[1], [2, 5], [3, 6], [4]]
[[1], [2, 5], [3], [4, 6]]
[[1, 6], [2], [3, 5], [4]]
[[1], [2, 6], [3, 5], [4]]
[[1], [2], [3, 5, 6], [4]]
[[1], [2], [3, 5], [4, 6]]
[[1, 6], [2], [3], [4, 5]]
[[1], [2, 6], [3], [4, 5]]
[[1], [2], [3, 6], [4, 5]]
[[1], [2], [3], [4, 5, 6]]
[[1, 4, 6], [2], [3], [5]]
[[1, 4], [2, 6], [3], [5]]
[[1, 4], [2], [3, 6], [5]]
[[1, 4], [2], [3], [5, 6]]
[[1, 6], [2, 4], [3], [5]]
[[1], [2, 4, 6], [3], [5]]
[[1], [2, 4], [3, 6], [5]]
[[1], [2, 4], [3], [5, 6]]
[[1, 6], [2], [3, 4], [5]]
[[1], [2, 6], [3, 4], [5]]
[[1], [2], [3, 4, 6], [5]]
[[1], [2], [3, 4], [5, 6]]
[[1, 3, 6], [2], [4], [5]]
[[1, 3], [2, 6], [4], [5]]
[[1, 3], [2], [4, 6], [5]]
[[1, 3], [2], [4], [5, 6]]
[[1, 6], [2, 3], [4], [5]]
[[1], [2, 3, 6], [4], [5]]
[[1], [2, 3], [4, 6], [5]]
[[1], [2, 3], [4], [5, 6]]
[[1, 2, 6], [3], [4], [5]]
[[1, 2], [3, 6], [4], [5]]
[[1, 2], [3], [4, 6], [5]]
[[1, 2], [3], [4], [5, 6]]
[[1, 4, 5], [2], [3], [6]]
[[1, 4], [2, 5], [3], [6]]
[[1, 4], [2], [3, 5], [6]]
[[1, 5], [2, 4], [3], [6]]
[[1], [2, 4, 5], [3], [6]]
[[1], [2, 4], [3, 5], [6]]
[[1, 5], [2], [3, 4], [6]]
[[1], [2, 5], [3, 4], [6]]
[[1], [2], [3, 4, 5], [6]]
[[1, 3, 5], [2], [4], [6]]
[[1, 3], [2, 5], [4], [6]]
[[1, 3], [2], [4, 5], [6]]
[[1, 5], [2, 3], [4], [6]]
[[1], [2, 3, 5], [4], [6]]
[[1], [2, 3], [4, 5], [6]]
[[1, 2, 5], [3], [4], [6]]
[[1, 2], [3, 5], [4], [6]]
[[1, 2], [3], [4, 5], [6]]
[[1, 3, 4], [2], [5], [6]]
[[1, 3], [2, 4], [5], [6]]
[[1, 4], [2, 3], [5], [6]]
[[1], [2, 3, 4], [5], [6]]
[[1, 2, 4], [3], [5], [6]]
[[1, 2], [3, 4], [5], [6]]
[[1, 2, 3], [4], [5], [6]]
'''