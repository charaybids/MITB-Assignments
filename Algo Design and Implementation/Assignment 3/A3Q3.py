import sys
from io import StringIO

def compute_transit_time(use_walking):
    res = [[3600] * n for _ in range(n)]
    if use_walking:
        for k, v in walking.items():
            res[k[0]][k[1]] = v
    return res

def compare_transit_time():
    res1 = compute_transit_time(False)
    res2 = compute_transit_time(True)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = res1[i][j] - res2[i][j]
    return res

s = sys.stdin.readline().split()
n, m = int(s[0]), int(s[1])
waiting = []
station_list = []
traveling = []
for _ in range(m):
    s = sys.stdin.readline().split()
    waiting.append(int(s[0]))
    st, tr = [], []
    for i in range(1, len(s), 2):
        st.append(int(s[i][1:]))
        if i + 1 < len(s):
            tr.append(int(s[i+1]))
    station_list.append(st)
    traveling.append(tr)
nn = int(sys.stdin.readline())
transfer = {}
for _ in range(nn):
    s = sys.stdin.readline().split()
    st = int(s[0][1:])
    transfer[st] = {}
    for i in range(1, len(s)):
        ss = s[i].split(':')
        l1, l2, t = int(ss[0][1:]), int(ss[1][1:]), int(ss[2])
        transfer[st][l1, l2], transfer[st][l2, l1] = t, t
mm = int(sys.stdin.readline())
walking = {}
for _ in range(mm):
    s = sys.stdin.readline().split()
    s1, s2, t = int(s[0][1:]), int(s[1][1:]), int(s[2])
    walking[s1, s2], walking[s2, s1] = t, t

transit_time = compare_transit_time()
for i in range(n):
    print(' '.join([str(j) for j in transit_time[i]]))

# Redirect stdout to capture print statements
old_stdout = sys.stdout
sys.stdout = StringIO()

# Capture the actual output
actual_output = sys.stdout.getvalue().strip().split('\n')

# Reset stdout
sys.stdout = old_stdout

# Read the expected output from A3Q3.out
with open('/A3Q3.out', 'r') as file:
    expected_output = file.read().strip().split('\n')

# Use assert to check the output
assert actual_output == expected_output, f"Output does not match. Expected: {expected_output}, Got: {actual_output}"

'''
Values to work with:
station_list: [[0, 1, 2, 3, 4], [3, 5, 6], [22, 21, 20, 19, 18, 17, 16, 5, 3, 10, 12, 13, 14, 15], [7, 6, 8, 9, 0, 25, 24, 14, 23], [11, 10, 9, 8, 26, 27, 28], [29, 27, 18, 30, 0, 13, 31]]
waiting: [140, 140, 99, 77, 69, 80]
transfer: {0: {(0, 3): 48, (3, 0): 48, (0, 5): 75, (5, 0): 75, (3, 5): 122, (5, 3): 122}, 3: {(0, 1): 24, (1, 0): 24, (0, 2): 66, (2, 0): 66, (1, 2): 66, (2, 1): 66}, 5: {(1, 2): 18, (2, 1): 18}, 6: {(1, 3): 99, (3, 1): 99}, 8: {(3, 4): 20, (4, 3): 20}, 9: {(3, 4): 20, (4, 3): 20}, 10: {(2, 4): 176, (4, 2): 176}, 13: {(2, 5): 118, (5, 2): 118}, 14: {(2, 3): 125, (3, 2): 125}, 18: {(2, 5): 40, (5, 2): 40}, 27: {(4, 5): 195, (5, 4): 195}}
traveling: [[90, 98, 86, 175], [122, 125], [177, 136, 186, 192, 72, 103, 89, 122, 224, 119, 78, 161, 187], [191, 183, 144, 126, 119, 108, 132, 145], [152, 130, 144, 129, 133, 245], [297, 117, 89, 134, 137, 141]]
walking: {(0, 20): 300, (20, 0): 300, (1, 20): 120, (20, 1): 120, (1, 9): 420, (9, 1): 420, (1, 10): 600, (10, 1): 600, (2, 9): 300, (9, 2): 300, (2, 10): 660, (10, 2): 660, (6, 16): 240, (16, 6): 240, (8, 16): 420, (16, 8): 420, (8, 17): 300, (17, 8): 300, (8, 18): 660, (18, 8): 660, (8, 30): 600, (30, 8): 600, (10, 21): 540, (21, 10): 540, (12, 20): 480, (20, 12): 480, (12, 21): 300, (21, 12): 300, (13, 21): 600, (21, 13): 600, (17, 26): 480, (26, 17): 480, (19, 30): 600, (30, 19): 600}

how to read the input file:
- first line: n, m is the number of stations and the number of lines in the input file
2 line to 7 line: waiting time for each station is the first value in each line, followed by the station numbers in the line, followed by the travel time between the stations
8 line: nn is the number of transfer times in the input file
9 line to 19 line: transfer time between lines
20 line: mm is the number of walking times in the input file
21 line to 51 line: walking time between stations  

so what to do:
- read the input file
- create a list of stataions, waiting times, transfer times, travel times, and walking times
- create a function to compute the transit time
- create a function to compare the transit time
- print the time it take for each station to travel to another station in the network
- do this in a 32x32 grid
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 49 520 421 421 0 0 0 0 0 0 0 0 0
where station 0 provides 49 seconds of time saved if we walk and train to station 20 and so on 
'''