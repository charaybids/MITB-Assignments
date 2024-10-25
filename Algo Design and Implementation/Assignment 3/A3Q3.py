import sys
import heapq

def compute_transit_time(use_walking):
    # Build the graph
    graph = [{} for _ in range(total_nodes)]
    # Add train edges
    for line_id in range(len(station_list)):
        st_list = station_list[line_id]
        tr_list = traveling[line_id]
        waiting_time = waiting[line_id]
        for idx in range(len(st_list)):
            station = st_list[idx]
            station_node = node_indices[station]
            line_node = node_indices[(station, line_id)]
            # Edge from station to (station, line) with waiting time
            graph[station_node][line_node] = waiting_time
            # If previous station exists
            if idx > 0:
                prev_station = st_list[idx - 1]
                travel_time = tr_list[idx - 1]
                u = node_indices[(prev_station, line_id)]
                v = node_indices[(station, line_id)]
                # Edge between (prev_station, line) and (station, line)
                graph[u][v] = travel_time
                graph[v][u] = travel_time
    # Add transfer edges
    for station in transfer:
        for (l1, l2), trans_time in transfer[station].items():
            node1 = node_indices[(station, l1)]
            node2 = node_indices[(station, l2)]
            waiting_time = waiting[l2]
            total_time = trans_time + waiting_time
            graph[node1][node2] = total_time
    # Add walking edges if use_walking is True
    if use_walking:
        for (s1, s2), walk_time in walking.items():
            node1 = node_indices[s1]
            node2 = node_indices[s2]
            graph[node1][node2] = walk_time
            graph[node2][node1] = walk_time

    # Debug: Print the graph structure
    print("Graph structure:")
    for i, edges in enumerate(graph):
        print(f"Node {i}: {edges}")

    # Compute shortest paths
    res = [[float('inf')] * n_stations for _ in range(n_stations)]
    for station in stations:
        station_idx = station_indices[station]
        station_node = node_indices[station]
        dist = dijkstra(graph, station_node, total_nodes)
        for dest_station in stations:
            dest_idx = station_indices[dest_station]
            res[station_idx][dest_idx] = dist[node_indices[dest_station]]
    return res

def compare_transit_time():
    res1 = compute_transit_time(use_walking=False)
    res2 = compute_transit_time(use_walking=True)
    n_stations = len(res1)
    res = [[0] * n_stations for _ in range(n_stations)]
    for i in range(n_stations):
        for j in range(n_stations):
            time_saving = res1[i][j] - res2[i][j]
            if time_saving < 0 or res1[i][j] == float('inf') or res2[i][j] == float('inf'):
                time_saving = 0
            res[i][j] = int(time_saving)
    return res

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v in graph[u]:
            alt = dist[u] + graph[u][v]
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(heap, (alt, v))

    # Debug: Print the distances from the start node
    print(f"Distances from node {start}: {dist}")

    return dist

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

# Prepare station indices
stations_set = set()
for st_list in station_list:
    for st in st_list:
        stations_set.add(st)
stations = list(stations_set)
stations.sort()
station_indices = {station: idx for idx, station in enumerate(stations)}
n_stations = len(stations)

# Build node indices
node_indices = {}
node_counter = 0
station_to_lines = {station: [] for station in stations}  # Initialize station_to_lines
for line_id, st_list in enumerate(station_list):
    for station in st_list:
        station_to_lines[station].append(line_id)

for station in stations:
    node_indices[station] = node_counter
    node_counter += 1
for station in stations:
    for line in station_to_lines[station]:
        node_indices[(station, line)] = node_counter
        node_counter += 1
total_nodes = node_counter

transit_time = compare_transit_time()
for i in range(n):
    print(' '.join([str(j) for j in transit_time[i]]))
