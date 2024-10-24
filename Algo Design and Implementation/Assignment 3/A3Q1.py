import sys

def min_shot(colors):
    n = len(colors)

    # Initialize a DP table to store the minimum shots for each subrange
    dp = [[float('inf')] * n for _ in range(n)]  # O(n^2), initializing an n x n matrix with infinity

    # Base cases: Single balls require 1 shot
    for i in range(n):  # O(n), filling the diagonal with 1
        dp[i][i] = 1

    # Base case for two adjacent balls  # O(n), since running n - 1 times
    for i in range(n - 1):
        dp[i][i + 1] = 1 if colors[i] == colors[i + 1] else 2

    # Fill the DP table for ranges of length 3 to n
    for length in range(3, n + 1):  # O(n^3), since running 3 for loops with O(n) times each
        # length of the subproblem
        for left in range(n - length + 1):
            right = left + length - 1

            # Case 1: Try merging the ends if colors[left] == colors[right]
            if colors[left] == colors[right]:
                dp[left][right] = dp[left + 1][right - 1]

            # Case 2: Try splitting the range at all possible midpoints
            for mid in range(left, right):
                dp[left][right] = min(dp[left][right], dp[left][mid] + dp[mid + 1][right])

    # Return the minimum number of shots needed to clear the entire sequence
    return dp[0][n - 1]



'''
def is_palindrome(lst):
    return lst == lst[::-1]

def find_largest_palindrome(arr):
    best_indices = (-1, -1)
    for start in range(len(arr)):
        for end in range(start + 2, len(arr) + 1):
            subarray = arr[start:end]
            if is_palindrome(subarray) and (end - start) > (best_indices[1] - best_indices[0]):
                best_indices = (start, end)
    return best_indices

def find_best_element_to_remove(arr, memo):
    min_steps = float('inf')
    best_index = -1

    for i in range(len(arr)):
        temp_arr = tuple(arr[:i] + arr[i+1:])
        if temp_arr not in memo:
            memo[temp_arr] = dynamic_palindrome_removal(list(temp_arr), memo)
        steps = memo[temp_arr]
        if steps < min_steps:
            min_steps = steps
            best_index = i

    return best_index

def dynamic_palindrome_removal(arr, memo=None):
    if memo is None:
        memo = {}
    steps = 0
    while len(arr) > 0:
        start, end = find_largest_palindrome(arr)
        if start != -1:
            arr = arr[:start] + arr[end:]
            steps += 1
        else:
            best_index = find_best_element_to_remove(arr, memo)
            if best_index != -1:
                arr.pop(best_index)
            else:
                arr.pop(0)
            steps += 1
    return steps
'''

num_line = int(sys.stdin.readline())

for _ in range(num_line):
    color_array = [int(s) for s in sys.stdin.readline().split()]
    print(min_shot(color_array))

