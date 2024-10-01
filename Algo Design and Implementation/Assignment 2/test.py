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
    
    # Recursive case with memoization
    memo[(n, k)] = k * stirling_second_kind(n - 1, k, memo) + stirling_second_kind(n - 1, k - 1, memo)
    return memo[(n, k)]

# Example usage
n = 5
k = 3
print(stirling_second_kind(n, k))  # Output: 25