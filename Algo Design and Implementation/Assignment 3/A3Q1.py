'''
Time Complexity Analysis:
The time complexity of the remove_palindrome function is O(N^3), where N is the length of the input array p_array.
This is because the function uses three nested loops to fill the DP table:
1. The outermost loop runs for subsequence lengths from 3 to N, which is O(N).
2. The middle loop runs for each starting index of the subsequence, which is also O(N).
3. The innermost loop runs for each possible partition point within the subsequence, which is again O(N).
Therefore, the overall time complexity is O(N^3).
'''

import sys

def remove_palindrome(p_array):
    p_length = len(p_array)

    dp_table = [[float('inf')] * p_length for _ in range(p_length)]  

    for index in range(p_length):  
        dp_table[index][index] = 1
   
    for index in range(p_length - 1):
        dp_table[index][index + 1] = 1 if p_array[index] == p_array[index + 1] else 2

    for subrange_length in range(3, p_length + 1): 
        
        for start in range(p_length - subrange_length + 1):
            end = start + subrange_length - 1
            
            if p_array[start] == p_array[end]:
                dp_table[start][end] = dp_table[start + 1][end - 1]
            
            for mid in range(start, end):
                dp_table[start][end] = min(dp_table[start][end], dp_table[start][mid] + dp_table[mid + 1][end])
    
    return dp_table[0][p_length - 1]

num_line = int(sys.stdin.readline())

for _ in range(num_line):
    p_array = [int(s) for s in sys.stdin.readline().split()]
    print(remove_palindrome(p_array))
