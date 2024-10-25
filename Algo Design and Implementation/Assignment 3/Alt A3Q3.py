import sys
import heapq
from itertools import count


def compute_transit_time(use_walking):
    graph = [{} for _ in range(n)]  # Adjacency list for each station

    # Build graph edges for transit lines
    for idx, stations in enumerate(station_list):
        wait_time = waiting[idx]
        travel_times = traveling[idx]
        line = idx  # Line index

        # Add edges between adjacent stations
        for i in range(len(stations) - 1):
            u = stations[i]
            v = stations[i + 1]
            travel_time = travel_times[i]
            # Edge from u to v
            if v not in graph[u]:
                graph[u][v] = []
            graph[u][v].append({
                'time': travel_time,
                'line': line
            })
            # Edge from v to u
            if u not in graph[v]:
                graph[v][u] = []
            graph[v][u].append({
                'time': travel_time,
                'line': line
            })

    # Add transfer times
    for station, transfers in transfer.items():
        for (line1, line2), t_time in transfers.items():
            for neighbor in graph[station]:
                for edge in graph[station][neighbor]:
                    if edge['line'] == line1:
                        # Add transfer to line2
                        edge['transfer'] = edge.get('transfer', {})
                        edge['transfer'][line2] = t_time

    # Add walking edges if allowed
    if use_walking:
        for (u, v), w_time in walking.items():
            # Edge from u to v
            if v not in graph[u]:
                graph[u][v] = []
            graph[u][v].append({
                'time': w_time,
                'line': 'walk'
            })
            # Edge from v to u
            if u not in graph[v]:
                graph[v][u] = []
            graph[v][u].append({
                'time': w_time,
                'line': 'walk'
            })

    # Initialize counter for heap entries
    entry_counter = count()

    # Compute shortest paths using Dijkstra's algorithm from each station
    res = [[float('inf')] * n for _ in range(n)]
    for s in range(n):
        distances = [float('inf')] * n
        hq = []
        # Initialize distances with waiting times for each line starting at station s
        for idx, stations in enumerate(station_list):
            if s in stations:
                wait_time = waiting[idx]
                heapq.heappush(hq, (wait_time, next(entry_counter), s, idx))  # (time, count, station, line)
        # Include walking start if allowed
        if use_walking:
            heapq.heappush(hq, (0, next(entry_counter), s, 'walk'))
        while hq:
            time, _, u, curr_line = heapq.heappop(hq)
            if distances[u] <= time:
                continue
            distances[u] = time
            for v in graph[u]:
                for edge in graph[u][v]:
                    next_line = edge['line']
                    t_time = edge['time']
                    total_time = time + t_time
                    # Add transfer time if changing lines
                    if curr_line != next_line and curr_line != 'walk' and next_line != 'walk':
                        transfer_time = edge.get('transfer', {}).get(next_line, None)
                        if transfer_time is not None:
                            total_time += transfer_time
                        else:
                            continue  # Can't transfer without transfer time
                    heapq.heappush(hq, (total_time, next(entry_counter), v, next_line))
        res[s] = distances
    return res

def compare_transit_time():
    res1 = compute_transit_time(False)
    res2 = compute_transit_time(True)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if res1[i][j] == float('inf') or res2[i][j] == float('inf'):
                res[i][j] = 0
            else:
                res[i][j] = int(res1[i][j] - res2[i][j]) if res1[i][j] > res2[i][j] else 0
    return res

s = sys.stdin.readline().split()
n, m = int(s[0]), int(s[1])
waiting = []
station_list = []
traveling = []
for _ in range(m):
    s = sys.stdin.readline().split()
    waiting.append(int(s[0]))
    st, tr = [], []
    for i in range(1, len(s), 2):
        st.append(int(s[i][1:]))
        if i + 1 < len(s):
            tr.append(int(s[i+1]))
    station_list.append(st)
    traveling.append(tr)
nn = int(sys.stdin.readline())
transfer = {}
for _ in range(nn):
    s = sys.stdin.readline().split()
    st = int(s[0][1:])
    transfer[st] = {}
    for i in range(1, len(s)):
        ss = s[i].split(':')
        l1, l2, t = int(ss[0][1:]), int(ss[1][1:]), int(ss[2])
        transfer[st][l1, l2], transfer[st][l2, l1] = t, t
mm = int(sys.stdin.readline())
walking = {}
for _ in range(mm):
    s = sys.stdin.readline().split()
    s1, s2, t = int(s[0][1:]), int(s[1][1:]), int(s[2])
    walking[s1, s2], walking[s2, s1] = t, t

transit_time = compare_transit_time()
for i in range(n):
    print(' '.join([str(j) for j in transit_time[i]]))