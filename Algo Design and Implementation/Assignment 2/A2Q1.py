import sys

def to_CBST(a):
    return '0 -1 -2 1'

num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]
    print(to_CBST(a))
