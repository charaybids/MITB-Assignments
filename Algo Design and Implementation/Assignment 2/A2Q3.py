import sys

def num_grouping(n, m, k):
    return 0

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, m, k = a[0], a[1], a[2]
    print(num_grouping(n, m, k))
