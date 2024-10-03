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

# Example usage
inputs = [
    (6, 1, 4),
    (6, 2, 4),
    (6, 3, 4),
]

for n, m, k in inputs:
    print(f"Number of ways to partition {n} students into {k} groups with {m} pairs of twins: {student_grouping(n, m, k)}")