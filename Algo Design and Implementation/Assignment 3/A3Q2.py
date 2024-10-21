import sys
import heapq

def project_selection(groups, init_cap):
    current_cap = init_cap
    
    # Initialize separate min-heaps and max-heaps for each group
    min_heaps = [[] for _ in groups]
    max_heaps = [[] for _ in groups]
    
    for i, group in enumerate(groups):
        # Add all projects to the min-heap based on their cost
        for project in group:
            heapq.heappush(min_heaps[i], (project[0], project[1]))
        
        # Transfer affordable projects to the max-heap based on their profit
        while min_heaps[i] and min_heaps[i][0][0] <= current_cap:
            cost, revenue = heapq.heappop(min_heaps[i])
            profit = revenue - cost
            heapq.heappush(max_heaps[i], (-profit, cost, revenue))
        
        if not max_heaps[i]:
            return "impossible"
        
        # Select the project with the highest profit
        best_project = heapq.heappop(max_heaps[i])
        current_cap += best_project[2] - best_project[1]
    
    return current_cap


a = [int(s) for s in sys.stdin.readline().split()]
cr = []
for _ in range(a[0]):
    cr.append([[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()])
init_cap = [int(s) for s in sys.stdin.readline().split()]
for i in range(a[1]):
    print(project_selection(cr, init_cap[i]))


'''
import sys

def project_selection(groups, init_cap):
    current_cap = init_cap
    for group in groups:
        # Filter projects that can be afforded with the current capital
        affordable_projects = [p for p in group if p[0] <= current_cap]
        if not affordable_projects:
            return "impossible"
        # Select the project with the highest profit (revenue - cost)
        best_project = max(affordable_projects, key=lambda p: p[1] - p[0])
        current_cap += best_project[1] - best_project[0]
    return current_cap

a = [int(s) for s in sys.stdin.readline().split()]
cr = []
for _ in range(a[0]):
    cr.append([[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()])
init_cap = [int(s) for s in sys.stdin.readline().split()]
for i in range(a[1]):
    print(project_selection(cr, init_cap[i]))
'''