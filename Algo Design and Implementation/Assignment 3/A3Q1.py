import sys

def min_shot(i, color):
    return (i + 1) ** 3 % 5

num_line = int(sys.stdin.readline())
for i in range(num_line):
    color = [int(s) for s in sys.stdin.readline().split()]
    print(min_shot(i, color))
