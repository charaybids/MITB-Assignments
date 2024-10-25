'''
Time Complexity Analysis:

( P ): Number of projects in a group.
( S ): Number of capital states.
( G ): Number of project groups.

optimize_capital_states:
- Sorting: O(S log S), Python's sorted() function uses Timsort with is O(n log n).
- Pruning Loop: O(S), iterating over sorted capital states.
- Total: O(S log S)

project_selection:
- Outer Loop (over project groups): O(G), where G is the number of project groups.
- Sorting each group: O(P log P), where P is the maximum number of projects in a group.
- Inner Loops:
  - Iterating over capital states: O(S)
  - Iterating over projects in a group: O(P)
  - Total for inner loops: O(S * P)
- Total for each group: O(P log P + S * P)
- Total for all groups: O(G * (P log P + S * P))

Overall Time Complexity:
- optimize_capital_states: O(S log S)
- project_selection: O(G * (P log P + S * P))
* Note that although the worst case is N**3 where G = P = S, 
the question states that G and P are at most 1000 with S at most 50, 
so the actual complexity is much lower.
'''

import sys

def optimize_capital_states(capital_states_cost):

    sorted_capital_states = sorted(capital_states_cost.items(), reverse=True)

    optimised_states = {}
    min_cost = float('inf')

    for capital, cost in sorted_capital_states:
        if cost < min_cost:
            optimised_states[capital] = cost
            min_cost = cost

    return optimised_states

def project_selection(project_groups, initial_capital):

    capital_state = {initial_capital: 0}  

    for group in project_groups:
        next_capital_state = {}  

        group.sort()

        for project_cost, project_revenue in group:
            
            for current_capital, previous_project_cost in capital_state.items():
                
                if current_capital >= project_cost and (previous_project_cost == 0 or project_cost > previous_project_cost):
                    
                    updated_capital = current_capital + (project_revenue - project_cost)

                    if updated_capital not in next_capital_state or next_capital_state[updated_capital] > project_cost:
                        
                        next_capital_state[updated_capital] = project_cost

        capital_state = optimize_capital_states(next_capital_state)

    return max(capital_state.keys()) if capital_state else "impossible"


a = [int(s) for s in sys.stdin.readline().split()]
cr = []
for _ in range(a[0]):
    cr.append([[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()])
init_cap = [int(s) for s in sys.stdin.readline().split()]
for i in range(a[1]):
    print(project_selection(cr, init_cap[i]))



