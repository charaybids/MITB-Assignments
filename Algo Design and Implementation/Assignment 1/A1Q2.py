'''
note for tmr
All largest disk with even numbers will move clockwise A B C A B C
All largest disk with odd numbers will move counter clockwise A C B A C B
the start location typically depends on the location of the largest peg

'''
'''
note for tmr
All largest disk with even numbers will move clockwise A B C A B C
All largest disk with odd numbers will move counter clockwise A C B A C B
the start location typically depends on the location of the largest peg

'''
import sys

def hanoi_count(n, start, end, aux, state):
    
    if n == 0:
        return 0
    largest_disk = n
    largest_disk_peg = None
    
    for i, peg in enumerate(state):
        
        for j in range(len(peg)):

            if peg and peg[j] == largest_disk:
                largest_disk_peg = i
                peg.pop()
                break
    if largest_disk_peg is None:
        return "Impossible"  # Impossible state
    if largest_disk_peg == end:
        result = hanoi_count(n - 1, aux, end, start, state)
        if result == "Impossible":
            return "Impossible"
        return (2 ** (n - 1)) + result
    elif largest_disk_peg == start:
        result = hanoi_count(n - 1, start, aux, end, state)
        if result == "Impossible":
            return "Impossible"
        return result
    else:
        return "Impossible"  # Impossible state

def solve_hanoi(n, state):
    Oddcombi = [(0, 2, 1), (0, 1, 2), (1, 0, 2),(2, 1, 0)]
    EvenCombi = [(0, 1, 2), (1, 0, 2), (1, 2, 0), (2, 0, 1)]
    
    #print(f"Processing state: {state} with {n} disks")
    labels = ['A', 'B', 'C']
    
    # Find the peg with the largest disk
    largest_disk_peg = None
    for i, peg in enumerate(state):
        if peg and peg[-1] == n:
            largest_disk_peg = i
            break
    
    if largest_disk_peg is None:
        #print("No valid combination found")
        return
    
    # Select combinations based on the parity of n
    combinations = Oddcombi if n % 2 == 1 else EvenCombi
    
    min_moves = float('inf')
    best_combination = None
    
    for start, end, aux in combinations:
        state_copy = [peg[:] for peg in state]  # Create a copy of the state
        moves = hanoi_count(n, start, end, aux, state_copy)
        
        if moves != "Impossible" and moves < min_moves:
            min_moves = moves
            best_combination = (start, end, aux)
    
    if best_combination:
        start, end, aux = best_combination
        print(f"{labels[start]} {min_moves}")
    else:
        print("impossible")
    
# Example usage:
num_case = int(sys.stdin.readline())

for _ in range(num_case):
    states = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    n = len(states[0]) + len(states[1]) + len(states[2])
    solve_hanoi(n, states)

