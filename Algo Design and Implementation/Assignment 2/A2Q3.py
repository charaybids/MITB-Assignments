
'''
Define the Recurrence Relation:

Let dp[n][k] be the number of ways to partition n students into k groups.
The recurrence relation for the Stirling numbers of the second kind is: [ S(n, k) = k \\cdot S(n-1, k) + S(n-1, k-1) ]
We need to modify this to account for the pairs of twins.
Initialize the Base Cases:

dp[0][0] = 1: There is one way to partition 0 students into 0 groups.
dp[n][0] = 0 for ( n > 0 ): There are no ways to partition more than 0 students into 0 groups.
dp[0][k] = 0 for ( k > 0 ): There are no ways to partition 0 students into more than 0 groups.
Modify the Recurrence for Twins:

If a pair of twins is placed in different groups, we use the recurrence relation as is.
If a pair of twins is placed in the same group, we need to subtract these cases.
Implement the Dynamic Programming Solution:

Use a 3D array dp[n][k][m] where m is the number of pairs of twins.
'''
from itertools import combinations

def stirling_second_kind(n, k):
    # Base cases
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    
    # Recursive case
    return k * stirling_second_kind(n - 1, k) + stirling_second_kind(n - 1, k - 1)

def is_valid_partition(partition, pairs):
    for group in partition:
        for a, b in pairs:
            if a in group and b in group:
                return False
    return True

def generate_partitions(n, k, pairs):
    if n == 0 and k == 0:
        return [[]]
    if n == 0 or k == 0:
        return []
    
    partitions = []
    
    # Case 1: Add the nth element to one of the existing k groups
    for partition in generate_partitions(n - 1, k, pairs):
        for i in range(k):
            new_partition = [group[:] for group in partition]
            new_partition[i].append(n)
            if is_valid_partition(new_partition, pairs):
                partitions.append(new_partition)
    
    # Case 2: Add the nth element as a new group
    for partition in generate_partitions(n - 1, k - 1, pairs):
        new_partition = [group[:] for group in partition]
        new_partition.append([n])
        if is_valid_partition(new_partition, pairs):
            partitions.append(new_partition)
    
    return partitions

def count_valid_partitions(n, k):
    pairs = list(combinations(range(1, n + 1), 2))
    partitions = generate_partitions(n, k, pairs)
    return len(partitions)

# Given tuples
tuples = [
    (4, 0, 3),
    (5, 1, 3),
    (6, 1, 4)
]

# Calculate the number of ways for each tuple
results = [(n, k, count_valid_partitions(n, k)) for n, _, k in tuples]

# Print the results
for n, k, result in results:
    print(f"Number of ways to partition {n} elements into {k} non-empty groups with constraints: {result}")
'''
import sys

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m, k = a[0], a[1], a[2]
    print(f"{n} {m} {k}")
'''

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