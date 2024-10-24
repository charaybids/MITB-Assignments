


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

# Test arrays
arrays = [
    [1, 2, 1],  # Steps: 1
    [1, 2, 3],  # Steps: 3
    [1, 2, 3, 4, 5, 5, 4, 2, 1],  # Steps: 2
    [1, 2, 3, 4, 5, 6, 7, 8, 9],  # Steps: 4
    [1, 3, 5, 6, 6, 2, 3, 5, 7, 1],  # Steps: 5
    [6, 8, 3, 9, 9, 7, 4, 2, 2, 2, 4, 4, 3, 3], # Steps: 7 fails when n = 14
    [3, 6, 6, 3, 3, 6, 1, 9, 7, 4, 1, 5, 5, 8, 9, 1, 9, 5, 2, 3]  # Steps: 9
]

# Running the function for each array
for arr in arrays:
    print(f"Generated Array: {arr}")
    steps = dynamic_palindrome_removal(arr)
    print(f"Steps: {steps}\n")


'''
# Test arrays
arrays = [
    [1, 2, 1],  # Steps: 1
    [1, 2, 3],  # Steps: 3
    [1, 2, 3, 4, 5, 5, 4, 2, 1],  # Steps: 2
    [1, 3, 5, 6, 6, 2, 5, 7, 1],  # Steps: 4
    [1, 3, 5, 6, 6, 2, 3, 5, 7, 1],  # Steps: 5
    [3, 6, 6, 3, 3, 6, 1, 9, 7, 4, 1, 5, 5, 8, 9, 1, 9, 5, 2, 3]  #Steps: 5
]

for arr in arrays:
    print(f"Generated Array: {arr}")
    steps = dynamic_palindrome_removal(arr)
    print(f"Steps: {steps}")

'''

# Test arrays
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

def find_longest_palindrome_subsequence(arr):
    n = len(arr)
    best_indices = (0, 0)

    for start in range(n):
        for end in range(start + 1, n + 1):
            subarray = arr[start:end]
            if is_palindrome(subarray) and (end - start) > (best_indices[1] - best_indices[0]):
                best_indices = (start, end)
    
    return best_indices

def find_best_element_to_remove(arr):
    start_index, end_index = find_longest_palindrome_subsequence(arr)
    end_index -= 1  # Adjust end_index to be inclusive

    while start_index < end_index:
        if arr[start_index] == arr[end_index]:
            start_index += 1
            end_index -= 1
        else:
            # Check which removal would result in a longer palindrome
            if is_palindrome(arr[start_index + 1:end_index + 1]):
                return start_index
            elif is_palindrome(arr[start_index:end_index]):
                return end_index
            else:
                # If neither removal results in a palindrome, choose the one that maximizes the palindrome length
                if len(arr[start_index + 1:end_index + 1]) > len(arr[start_index:end_index]):
                    return start_index
                else:
                    return end_index
    return None

def dynamic_palindrome_removal(arr):
    steps = 0
    while len(arr) > 0:
        start, end = find_largest_palindrome(arr)
        if start != -1:
            print(f"Removing palindrome {arr[start:end]} from indices ({start}, {end-1})")
            arr = arr[:start] + arr[end:]
            steps += 1
        else:
            index_to_remove = find_best_element_to_remove(arr)
            if index_to_remove is not None:
                print(f"Removing element {arr[index_to_remove]} at index {index_to_remove}")
                arr.pop(index_to_remove)
            else:
                print(f"Removing first element {arr[0]}")
                arr.pop(0)
            steps += 1
    return steps


arrays = [
    [1, 2, 1],  # Steps: 1
    [1, 2, 3],  # Steps: 3
    [1, 2, 3, 4, 5, 5, 4, 2, 1],  # Steps: 2
    [1, 3, 5, 6, 6, 2, 5, 7, 1],  # Steps: 4
    [1, 3, 5, 6, 6, 2, 3, 5, 7, 1],  # Steps: 5
    [3, 6, 6, 3, 3, 6, 1, 9, 7, 4, 1, 5, 5, 8, 9, 1, 9, 5, 2, 3]  #Steps: 5
    ]

import random as r   

arrays = []
for i in range(5):
    arrays.append([r.randint(1, 10) for _ in range(11)])

for arr in arrays:
    print(f"Generated Array: {arr}")
    steps = dynamic_palindrome_removal(arr)
    print(f"Steps: {steps}")
    print("\n")

'''