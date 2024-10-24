'''
import sys

def project_selection(groups, init_cap):
    dp = {init_cap: init_cap}
    
    for group in groups:
        next_dp = {}
        for cap in dp:
            for cost, revenue in group:
                if cost <= cap:
                    profit = revenue - cost
                    new_cap = cap + profit
                    if new_cap not in next_dp or next_dp[new_cap] < new_cap:
                        next_dp[new_cap] = new_cap
        if not next_dp:
            return "impossible"
        dp = next_dp
    
    return max(dp.values())

a = [int(s) for s in sys.stdin.readline().split()]
cr = []
for _ in range(a[0]):
    cr.append([[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()])
start_cap = [int(s) for s in sys.stdin.readline().split()]
for i in range(a[1]):
    print(project_selection(cr,start_cap[i]))



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