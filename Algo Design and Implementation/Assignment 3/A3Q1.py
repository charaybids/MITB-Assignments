import sys

def is_palindrome(arr, start, end):
    while start < end:
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1
    return True

def find_min_shot(color, start, end, memo):
    if (start, end) in memo:
        return memo[(start, end)]
    
    if is_palindrome(color, start, end):
        memo[(start, end)] = 1
        return 1
    
    min_shots = float('inf')
    for k in range(start, end):
        left_shots = find_min_shot(color, start, k, memo)
        right_shots = find_min_shot(color, k + 1, end, memo)
        min_shots = min(min_shots, left_shots + right_shots)
    
    memo[(start, end)] = min_shots
    return min_shots

def min_shot(color):
    n = len(color)
    dynamic_table = {}
    return find_min_shot(color, 0, n-1, dynamic_table)

array1 = [1, 3, 5, 6, 6, 2, 5, 7, 1]
print(min_shot(array1))

    
'''
num_line = int(sys.stdin.readline())

for _ in range(num_line):
    color = [int(s) for s in sys.stdin.readline().split()]
    print(min_shot(color))
'''    

