
'''
Define the Recurrence Relation:

The recurrence relation for the Stirling numbers of the second kind is: [ S(n, k) = k \\cdot S(n-1, k) + S(n-1, k-1) ]
But however this is insufficient. 

we will need to use the principle of inclusion exclusion accounts for the constraints 
that none of the ( m ) pairs of twins can be in the same group. 
The general formula for the number of ways to partition ( n ) students into ( k ) groups without placing any of the 
( m ) pairs of twins in the same group is 

Summation of ( (-1)^i * Binominal(m, i) * S(n-i, k) ) for i = 0 to m.
for m = 3
S(n, k) = S(n-3, k) - Binominal(3, 1) * S(n-2, k) + Binominal(3, 2) * S(n-1, k) - Binominal(3, 3) * S(n, k)

for m = 4
S(n,k) = S(n-4, k) - Binominal(4, 1) * S(n-3, k) + Binominal(4, 2) * S(n-2, k) - Binominal(4, 3) * S(n-1, k) + Binominal(4, 4) * S(n, k)

Bases Cases:
Case 1: if n == 0 and k == 0:
This case returns 1 because there is exactly one way to partition an empty set (0 elements) into 0 non-empty subsets, which is the empty partition.

Case 2: if n == 0 or k == 0:
This case returns 0 because:
If n == 0 and k != 0, there are no ways to partition 0 elements into a positive number of non-empty subsets.
If k == 0 and n != 0, there are no ways to partition a positive number of elements into 0 non-empty subsets.

assuming the comb function isO(1) time complexity, and the the time complexity of the memoization is O(n*k) hence the highest is O(n * k).

'''
import sys
from math import comb

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
    total_num = 0
    for i in range(m + 1):
        sign = (-1) ** i
        total_num += sign * comb(m, i) * stirling_second_kind(n - i, k)
    return total_num

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m, k = a[0], a[1], a[2]
    print(student_grouping(n, m, k))