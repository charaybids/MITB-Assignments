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
a = [int(s) for s in sys.stdin.readline().split()]
cr = []
for _ in range(a[0]):
    cr.append([[int(t) for t in s.split(':')] for s in sys.stdin.readline().split()])
init_cap = [int(s) for s in sys.stdin.readline().split()]
for i in range(a[1]):
    print("Cr: ", cr[i])
    print(init_cap[i])
'''