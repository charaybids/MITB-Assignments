import sys
import heapq

'''
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
        transfer[st][(l1, l2)] = t
        transfer[st][(l2, l1)] = t
mm = int(sys.stdin.readline())
walking = {}
for _ in range(mm):
    s = sys.stdin.readline().split()
    s1, s2, t = int(s[0][1:]), int(s[1][1:]), int(s[2])
    walking[(s1, s2)] = t
    walking[(s2, s1)] = t

# Map stations to lines
station_to_lines = {}
for line_idx, line in enumerate(station_list):
    for station in line:
        station_to_lines.setdefault(station, set()).add(line_idx)
'''
# Initialize the graphs
G = {}
G_with_walking = {}


# Station lists and attributes
station_list = [
    [0, 1, 2, 3, 4],    # Line 0
    [3, 5, 6],          # Line 1
    [22, 21, 20, 19, 18, 17, 16, 5, 3, 10, 12, 13, 14, 15],  # Line 2
    [7, 6, 8, 9, 0, 25, 24, 14, 23],    # Line 3
    [11, 10, 9, 8, 26, 27, 28],    # Line 4
    [29, 27, 18, 30, 0, 13, 31]    # Line 5
]

waiting = [140, 140, 99, 77, 69, 80]  # Wait times for each line

traveling = [
    [90, 98, 86, 175],    # Line 0
    [122, 125],    # Line 1
    [177, 136, 186, 192, 72, 103, 89, 122, 224, 119, 78, 161, 187],    # Line 2
    [191, 183, 144, 126, 119, 108, 132, 145],    # Line 3
    [152, 130, 144, 129, 133, 245],    # Line 4
    [297, 117, 89, 134, 137, 141]   # Line 5
]

# Add transfer times and wait times when transferring
transfer = {
    0: {(0, 3): 48, (3, 0): 48, (0, 5): 75, (5, 0): 75, (3, 5): 122, (5, 3): 122},
    3: {(0, 1): 24, (1, 0): 24, (0, 2): 66, (2, 0): 66, (1, 2): 66, (2, 1): 66},
    5: {(1, 2): 18, (2, 1): 18},
    6: {(1, 3): 99, (3, 1): 99},
    8: {(3, 4): 20, (4, 3): 20},
    9: {(3, 4): 20, (4, 3): 20},
    10: {(2, 4): 176, (4, 2): 176},
    13: {(2, 5): 118, (5, 2): 118},
    14: {(2, 3): 125, (3, 2): 125},
    18: {(2, 5): 40, (5, 2): 40},
    27: {(4, 5): 195, (5, 4): 195}
}

# Add walking times
walking = {
    (0, 20): 300, (20, 0): 300,
    (1, 20): 120, (20, 1): 120,
    (1, 9): 420, (9, 1): 420,
    (1, 10): 600, (10, 1): 600,
    (2, 9): 300, (9, 2): 300,
    (2, 10): 660, (10, 2): 660,
    (6, 16): 240, (16, 6): 240,
    (8, 16): 420, (16, 8): 420,
    (8, 17): 300, (17, 8): 300,
    (8, 18): 660, (18, 8): 660,
    (8, 30): 600, (30, 8): 600,
    (10, 21): 540, (21, 10): 540,
    (12, 20): 480, (20, 12): 480,
    (12, 21): 300, (21, 12): 300,
    (13, 21): 600, (21, 13): 600,
    (17, 26): 480, (26, 17): 480,
    (19, 30): 600, (30, 19): 600
}

# Helper function to add edges to the graph
def add_edge(graph, u, v, weight, description=""):
    graph.setdefault(u, []).append((v, weight))
    graph.setdefault(v, []).append((u, weight))  # Since the graph is undirected
    
# Map stations to lines
station_to_lines = {}
for line_idx, line in enumerate(station_list):
    for station in line:
        station_to_lines.setdefault(station, set()).add(line_idx)

# Add nodes and edges for each line separately
for line_idx, line in enumerate(station_list):
    # Add edges between consecutive stations on the same line
    for i in range(len(line)):
        u = (line[i], line_idx)
        G.setdefault(u, [])
        G_with_walking.setdefault(u, [])
        if i < len(line) - 1:
            v = (line[i + 1], line_idx)
            travel_time = traveling[line_idx][i]
            description = f"Line {line_idx}, between stations {line[i]} and {line[i+1]}"
            add_edge(G, u, v, travel_time, description)
            add_edge(G_with_walking, u, v, travel_time, description)

# Add transfer edges with transfer times and waiting times
for station, lines_at_station in station_to_lines.items():
    lines = list(lines_at_station)
    for line_i in lines:
        for line_j in lines:
            if line_i != line_j:
                transfer_time = transfer.get(station, {}).get((line_i, line_j), 0)
                wait_time = waiting[line_j]
                total_transfer_time = transfer_time + wait_time
                u = (station, line_i)
                v = (station, line_j)
                description = f"Transfer at station {station} from line {line_i} to line {line_j}"
                add_edge(G, u, v, total_transfer_time, description)
                add_edge(G_with_walking, u, v, total_transfer_time, description)

# Add walking edges to the graph with walking
for (u_station, v_station), walk_time in walking.items():
    lines_u = station_to_lines[u_station]
    lines_v = station_to_lines[v_station]
    for line_u in lines_u:
        for line_v in lines_v:
            u = (u_station, line_u)
            v = (v_station, line_v)
            description = f"Walking from station {u_station} (line {line_u}) to station {v_station} (line {line_v})"
            add_edge(G_with_walking, u, v, walk_time, description)

# Dijkstra's algorithm
def dijkstra(graph, start_nodes, end_nodes, initial_waiting_times):
    heap = []
    visited = {}
    for start in start_nodes:
        initial_wait = initial_waiting_times.get(start, 0)
        heapq.heappush(heap, (initial_wait, start, None))
        print(f"Starting node: {start} with initial cost {initial_wait}")

    while heap:
        cost, u, prev = heapq.heappop(heap)
        if u in visited:
            continue
        visited[u] = (cost, prev)
        print(f"Visiting node: {u} with cost: {cost}")

        if u in end_nodes:
            print(f"Reached end node: {u} with cost: {cost}")
            break

        for v, weight in graph.get(u, []):
            if v not in visited:
                new_cost = cost + weight
                heapq.heappush(heap, (new_cost, v, u))
                print(f"Considering edge from {u} to {v} with weight {weight}. New cost: {new_cost}")

    # Construct the path and return the minimum cost
    min_cost = float('inf')
    min_path = None
    for end in end_nodes:
        if end in visited and visited[end][0] < min_cost:
            min_cost = visited[end][0]
            min_path = []
            node = end
            while node is not None:
                min_path.append(node)
                node = visited[node][1]
            min_path.reverse()

    print(f"Minimum cost: {min_cost}")
    print(f"Path: {min_path}")
    return min_cost, min_path

# Example usage of the compute_shortest_time function
source_station = 0  # S0
dest_station = 20   # S22

source_nodes = [(source_station, line_idx) for line_idx in station_to_lines[source_station]]
dest_nodes = set([(dest_station, line_idx) for line_idx in station_to_lines[dest_station]])
initial_waiting_times = {idx: wait for idx, wait in enumerate(waiting)}

min_time_no_walking, path_no_walking = dijkstra(G, source_nodes, dest_nodes, initial_waiting_times)
min_time_with_walking, path_with_walking = dijkstra(G_with_walking, source_nodes, dest_nodes, initial_waiting_times)

print(f"Path without walking: {path_no_walking}\n") #80 + 134 + 89 + 40 + 99 + 192 + 186 = 820
print(f"minimum time without walking: {min_time_no_walking} seconds\n")

print(f"Path with walking: {path_with_walking}\n") #300
print(f"Minimum total time with walking: {min_time_with_walking} seconds\n")

print("Difference in time between the two paths is", min_time_no_walking - min_time_with_walking)



'''
# Get all stations
all_stations = list(station_to_lines.keys())
n_stations = max(all_stations) + 1

# Initialize the total_times matrices without using numpy
total_times_no_walking = [[float('inf')] * n_stations for _ in range(n_stations)]
total_times_with_walking = [[float('inf')] * n_stations for _ in range(n_stations)]

# Helper function to get nodes for a station
def get_nodes(station):
    return [(station, line_idx) for line_idx in station_to_lines[station]]

# Compute shortest times between all stations without walking
for i in all_stations:
    source_nodes = get_nodes(i)
    for j in all_stations:
        if i != j:
            dest_nodes = set(get_nodes(j))
            min_time, _ = dijkstra(G, source_nodes, dest_nodes)
            total_times_no_walking[i][j] = min_time
        else:
            total_times_no_walking[i][j] = 0  # Time from a station to itself is zero

# Compute shortest times between all stations with walking
for i in all_stations:
    source_nodes = get_nodes(i)
    for j in all_stations:
        if i != j:
            dest_nodes = set(get_nodes(j))
            min_time, _ = dijkstra(G_with_walking, source_nodes, dest_nodes)
            total_times_with_walking[i][j] = min_time
        else:
            total_times_with_walking[i][j] = 0  # Time from a station to itself is zero

# Compute the difference in travel times
difference_in_times = [[0] * n_stations for _ in range(n_stations)]
for i in range(n_stations):
    for j in range(n_stations):
        if total_times_no_walking[i][j] > total_times_with_walking[i][j]:
            diff = total_times_no_walking[i][j] - total_times_with_walking[i][j]
            difference_in_times[i][j] = diff
        else:
            difference_in_times[i][j] = 0

# Output the differences
n = len(difference_in_times)  # Number of stations
for row in difference_in_times[:n]:
    print(' '.join(map(lambda x: str(int(x)), row[:n])))
'''