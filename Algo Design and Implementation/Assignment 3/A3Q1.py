import sys

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


num_line = int(sys.stdin.readline())

for _ in range(num_line):
    color_array = [int(s) for s in sys.stdin.readline().split()]
    print(dynamic_palindrome_removal(color_array))

