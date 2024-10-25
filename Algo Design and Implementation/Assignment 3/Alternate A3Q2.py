
'''
import sys


Prune the dp dictionary to keep only the best capital states.

def prune_dp(dp):
    # Prune suboptimal states
    sorted_items = sorted(dp.items(), key=lambda x: (-x[0], x[1]))
    pruned_dp = {}
    min_cost = float('inf')
    for capital, cost in sorted_items:
        if cost < min_cost:
            pruned_dp[capital] = cost
            min_cost = cost
    return pruned_dp

def project_selection(cr, initial_capital):
    dp = {initial_capital: 0}  # Initialize hashtable: capital -> total cost
    for group in cr:
        next_dp = {}
        for cost, revenue in group:
            for capital in dp:
                if cost <= capital:
                    new_capital = capital + revenue - cost
                    total_cost = dp[capital] + cost
                    if new_capital not in next_dp or total_cost < next_dp[new_capital]:
                        next_dp[new_capital] = total_cost
        if not next_dp:
            return "impossible"
        dp = prune_dp(next_dp)  # Prune suboptimal states
    return max(dp.keys())


a = [int(s) for s in sys.stdin.readline().split()]
cr = []
for _ in range(a[0]):
    cr.append([[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()])
start_cap = [int(s) for s in sys.stdin.readline().split()]
for i in range(a[1]):
    print(project_selection(cr,start_cap[i]))
'''


'''
import sys

def project_selection(groups, init_cap):
    memo = {}
    
    def dfs(group_index, current_cap):
        if group_index == len(groups):
            return current_cap
        key = (group_index, current_cap)
        if key in memo:
            return memo[key]
        
        max_cap = -1
        for cost, revenue in groups[group_index]:
            if cost <= current_cap:
                profit = revenue - cost
                new_cap = current_cap + profit
                # Prune paths that cannot lead to a better solution
                if new_cap > max_cap:
                    next_cap = dfs(group_index + 1, new_cap)
                    if next_cap > max_cap:
                        max_cap = next_cap
        
        memo[key] = max_cap
        return max_cap
    
    result = dfs(0, init_cap)
    return result if result != -1 else "impossible"

# Read input data
a = [int(s) for s in sys.stdin.readline().split()]
cr = []
for _ in range(a[0]):
    cr.append([[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()])
start_cap = [int(s) for s in sys.stdin.readline().split()]
for i in range(a[1]):
    print(project_selection(cr,start_cap[i]))

'''


'''
import sys
import heapq

def project_selection(groups, init_cap):
    current_cap = init_cap
    
    for group in groups:
        min_heap = []
        max_heap = []
        
        # Add all projects to the min-heap based on their cost
        for project in group:
            heapq.heappush(min_heap, (project[0], project[1]))
        
        # Transfer affordable projects to the max-heap based on their profit
        while min_heap and min_heap[0][0] <= current_cap:
            cost, revenue = heapq.heappop(min_heap)
            profit = revenue - cost
            heapq.heappush(max_heap, (-profit, cost, revenue))
        
        if not max_heap:
            return "impossible"
        
        # Select the project with the highest profit
        best_project = heapq.heappop(max_heap)
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