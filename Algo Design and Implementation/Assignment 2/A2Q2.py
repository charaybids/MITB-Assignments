"""
To solve this problem, we can use a max-heap to always select the project with the highest profit 
that can be afforded with the current capital. Here is the step-by-step plan:

1. Parse the input to get the number of projects and scenarios.

2. Parse the list of projects into a list of tuples (cost, revenue).

3. For each scenario, initialize the current capital and the number of projects to select.

4. Use a min-heap to keep track of affordable projects based on their cost.

5. Use a max-heap to select the project with the highest profit among the affordable projects.

6. For each project selection, update the current capital and repeat until the required number of 
projects are selected or no more projects can be afforded.

7. Print the final capital or "impossible" if not enough projects can be selected.

Reading Input:

input = sys.stdin.read().splitlines(): This reads all input lines. If there are n lines, this operation is O(n).
n, scenarios = map(int, input[0].split()): This splits the first line and maps it to integers. This is O(1).
projects = [tuple(map(int, s.split(':'))) for s in input[1].split()]: This splits the second line and maps each part to integers. If there are m projects, this operation is O(m).
scenarios_data = [tuple(map(int, s.split())) for s in input[2:]]: This processes the remaining lines. If there are scenarios lines, this operation is O(scenarios).
Processing Each Scenario:

The outer loop for initial_capital, k in scenarios_data: runs scenarios times.
Inside the loop, project_selection(projects, initial_capital, k) is called.
Inside project_selection Function:

heapq.heappush(max_heap, (-profit, cost, revenue)): This operation is O(log m) for each push.
heapq.heappop(max_heap): This operation is O(log m) for each pop.
The loop that processes projects runs k times, and within each iteration, it performs a heappush and a heappop.
Combining these, the time complexity for processing each scenario is:

O(m log m) for the heap operations within the loop that runs k times.
Thus, the overall time complexity for the entire code is:

O(k * log m)

online Judge
8/8 Accepted for long and short test cases

"""

import sys
import heapq

def project_selection(projects, initial_capital, k):
    min_heap = []
    max_heap = []
    
    # Add all projects to the min-heap based on their cost
    for cost, revenue in projects:
        heapq.heappush(min_heap, (cost, revenue))
    
    current_capital = initial_capital
    
    for _ in range(k):
        # Move all affordable projects to the max-heap based on their profit
        while min_heap and min_heap[0][0] <= current_capital:
            cost, revenue = heapq.heappop(min_heap)
            profit = revenue - cost
            heapq.heappush(max_heap, (-profit, cost, revenue))
        
        # If no projects are affordable, return "impossible"
        if not max_heap:
            return "impossible"
        
        # Select the project with the highest profit
        profit, cost, revenue = heapq.heappop(max_heap)
        current_capital += -profit
    
    return current_capital

# Read input
input = sys.stdin.read().splitlines()
n, scenarios = map(int, input[0].split())
projects = [tuple(map(int, s.split(':'))) for s in input[1].split()]
scenarios_data = [tuple(map(int, s.split())) for s in input[2:]]

# Process each scenario
for initial_capital, k in scenarios_data:
    result = project_selection(projects, initial_capital, k)
    print(result)