import sys
import networkx as nx
import numpy as np

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

#LETS GO!!

# Map stations to lines
station_to_lines = {}
for line_idx, line in enumerate(station_list):
    for station in line:
        station_to_lines.setdefault(station, set()).add(line_idx)

# Initialize the graph
G = nx.Graph()

# Add nodes and edges for each line separately
for line_idx, line in enumerate(station_list):
    # Create nodes with (station, line)
    for station in line:
        G.add_node((station, line_idx))
    # Add edges between consecutive stations on the same line
    for i in range(len(line) - 1):
        u = (line[i], line_idx)
        v = (line[i + 1], line_idx)
        travel_time = traveling[line_idx][i]
        G.add_edge(u, v, weight=travel_time)


for station, lines_at_station in station_to_lines.items():
    lines = list(lines_at_station)
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line_i = lines[i]
            line_j = lines[j]
            # Get transfer time if available
            transfer_time = 0
            if station in transfer:
                transfer_dict = transfer[station]
                transfer_time = transfer_dict.get((line_i, line_j), transfer_dict.get((line_j, line_i), 0))
            # Add wait time for the new line (line_j)
            wait_time = waiting[line_j]
            total_transfer_time = transfer_time + wait_time
            u = (station, line_i)
            v = (station, line_j)
            G.add_edge(u, v, weight=total_transfer_time)

# Add walking edges to the graph
G_with_walking = G.copy()
for (u_station, v_station), walk_time in walking.items():
    lines_u = station_to_lines[u_station]
    lines_v = station_to_lines[v_station]
    for line_u in lines_u:
        for line_v in lines_v:
            u = (u_station, line_u)
            v = (v_station, line_v)
            G_with_walking.add_edge(u, v, weight=walk_time)

# Function to compute shortest path time without walking
def compute_shortest_time_no_walking(G, source_station, dest_station):
    min_total_time = float('inf')
    best_path = None

    source_nodes = [(source_station, line_idx) for line_idx in station_to_lines[source_station]]
    dest_nodes = [(dest_station, line_idx) for line_idx in station_to_lines[dest_station]]

    for source_node in source_nodes:
        for dest_node in dest_nodes:
            try:
                path = nx.dijkstra_path(G, source_node, dest_node, weight='weight')
                travel_time = 0
                total_time = 0
                current_line = path[0][1]

                # Check if starting node is same as the first movement line
                if len(path) > 1 and path[1][1] == current_line:
                    total_time += waiting[current_line]  # Add wait time at the start
                else:
                    # Starting with a transfer, add transfer time only
                    transfer_time = transfer.get(source_station, {}).get((current_line, path[1][1]), 0)
                    total_time += transfer_time
                    current_line = path[1][1]

                for i in range(len(path) - 1):
                    u = path[i]
                    v = path[i + 1]
                    edge_data = G.get_edge_data(u, v)
                    edge_weight = edge_data['weight']
                    travel_time += edge_weight

                    next_line = v[1]
                    if next_line != current_line:
                        # Add transfer time when changing lines
                        transfer_time = transfer.get(u[0], {}).get((current_line, next_line), 0)
                        total_time += transfer_time
                        current_line = next_line

                total_time += travel_time

                if total_time < min_total_time:
                    min_total_time = total_time
                    best_path = path
            except nx.NetworkXNoPath:
                continue

    return min_total_time, best_path

# Function to compute shortest path time with walking
def compute_shortest_time_with_walking(G, source_station, dest_station):
    min_total_time = float('inf')
    best_path = None

    source_nodes = [(source_station, line_idx) for line_idx in station_to_lines[source_station]]
    dest_nodes = [(dest_station, line_idx) for line_idx in station_to_lines[dest_station]]

    for source_node in source_nodes:
        for dest_node in dest_nodes:
            try:
                path = nx.dijkstra_path(G, source_node, dest_node, weight='weight')
                travel_time = 0
                total_time = 0
                current_line = path[0][1]

                # Check if starting node is same as the first movement line
                if len(path) > 1 and path[1][1] == current_line:
                    total_time += waiting[current_line]  # Add wait time at the start
                else:
                    # Starting with a transfer, add transfer time only
                    transfer_time = transfer.get(source_station, {}).get((current_line, path[1][1]), 0)
                    total_time += transfer_time
                    current_line = path[1][1]

                for i in range(len(path) - 1):
                    u = path[i]
                    v = path[i + 1]
                    edge_data = G.get_edge_data(u, v)
                    edge_weight = edge_data['weight']
                    travel_time += edge_weight

                    next_line = v[1]
                    if next_line != current_line:
                        # Add transfer time when changing lines
                        transfer_time = transfer.get(u[0], {}).get((current_line, next_line), 0)
                        total_time += transfer_time
                        current_line = next_line

                total_time += travel_time

                if total_time < min_total_time:
                    min_total_time = total_time
                    best_path = path
            except nx.NetworkXNoPath:
                continue

    return min_total_time, best_path

# Compute the full travel time matrix between all stations without walking
all_stations = list(station_to_lines.keys())
n_stations = max(all_stations) + 1

# Initialize the total_times matrix
total_times_no_walking = np.full((n_stations, n_stations), np.inf)
total_times_with_walking = np.full((n_stations, n_stations), np.inf)

# Compute shortest times between all stations without walking
for i in all_stations:
    for j in all_stations:
        if i != j:
            min_time, _ = compute_shortest_time_no_walking(G, i, j)
            total_times_no_walking[i][j] = min_time
        else:
            total_times_no_walking[i][j] = 0  # Time from a station to itself is zero

# Compute shortest times between all stations with walking
for i in all_stations:
    for j in all_stations:
        if i != j:
            min_time, _ = compute_shortest_time_with_walking(G_with_walking, i, j)
            total_times_with_walking[i][j] = min_time
        else:
            total_times_with_walking[i][j] = 0  # Time from a station to itself is zero

# Compute the difference in travel times between all stations
difference_in_times = np.zeros((n_stations, n_stations))
for i in range(len(total_times_no_walking)):
    for j in range(len(total_times_no_walking[i])):
        if total_times_no_walking[i][j] > total_times_with_walking[i][j]:
            difference_in_times[i][j] = (total_times_no_walking[i][j] - total_times_with_walking[i][j])
        else:
            difference_in_times[i][j] = 0
            
for i in range(n):
    print(' '.join([str(int(j)) for j in difference_in_times[i]]))            


'''
Values to work with:
station_list: [[0, 1, 2, 3, 4], [3, 5, 6], [22, 21, 20, 19, 18, 17, 16, 5, 3, 10, 12, 13, 14, 15], [7, 6, 8, 9, 0, 25, 24, 14, 23], [11, 10, 9, 8, 26, 27, 28], [29, 27, 18, 30, 0, 13, 31]]
waiting: [140, 140, 99, 77, 69, 80]
transfer: {0: {(0, 3): 48, (3, 0): 48, (0, 5): 75, (5, 0): 75, (3, 5): 122, (5, 3): 122}, 3: {(0, 1): 24, (1, 0): 24, (0, 2): 66, (2, 0): 66, (1, 2): 66, (2, 1): 66}, 5: {(1, 2): 18, (2, 1): 18}, 6: {(1, 3): 99, (3, 1): 99}, 8: {(3, 4): 20, (4, 3): 20}, 9: {(3, 4): 20, (4, 3): 20}, 10: {(2, 4): 176, (4, 2): 176}, 13: {(2, 5): 118, (5, 2): 118}, 14: {(2, 3): 125, (3, 2): 125}, 18: {(2, 5): 40, (5, 2): 40}, 27: {(4, 5): 195, (5, 4): 195}}
traveling: [[90, 98, 86, 175], [122, 125], [177, 136, 186, 192, 72, 103, 89, 122, 224, 119, 78, 161, 187], [191, 183, 144, 126, 119, 108, 132, 145], [152, 130, 144, 129, 133, 245], [297, 117, 89, 134, 137, 141]]
walking: {(0, 20): 300, (20, 0): 300, (1, 20): 120, (20, 1): 120, (1, 9): 420, (9, 1): 420, (1, 10): 600, (10, 1): 600, (2, 9): 300, (9, 2): 300, (2, 10): 660, (10, 2): 660, (6, 16): 240, (16, 6): 240, (8, 16): 420, (16, 8): 420, (8, 17): 300, (17, 8): 300, (8, 18): 660, (18, 8): 660, (8, 30): 600, (30, 8): 600, (10, 21): 540, (21, 10): 540, (12, 20): 480, (20, 12): 480, (12, 21): 300, (21, 12): 300, (13, 21): 600, (21, 13): 600, (17, 26): 480, (26, 17): 480, (19, 30): 600, (30, 19): 600}

how to read the input file:
- first line: n, m is the number of stations and the number of lines in the input file
2 line to 7 line: waiting time for each station is the first value in each line, followed by the station numbers in the line, followed by the travel time between the stations
8 line: nn is the number of transfer times in the input file
9 line to 19 line: transfer time between lines
20 line: mm is the number of walking times in the input file
21 line to 51 line: walking time between stations  

so what to do:
- read the input file
- create a list of stataions, waiting times, transfer times, travel times, and walking times
- create a function to compute the transit time
- create a function to compare the transit time
- print the time it take for each station to travel to another station in the network
- do this in a 32x32 grid
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 49 520 421 421 0 0 0 0 0 0 0 0 0
where station 0 provides 49 seconds of time saved if we walk and train to station 20 and so on 
'''