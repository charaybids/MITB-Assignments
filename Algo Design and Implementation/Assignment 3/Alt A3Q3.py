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

# Shortest path computation functions remain simplified
def compute_shortest_time_no_walking(G, source_station, dest_station):
    min_total_time = float('inf')
    best_path = None

    source_nodes = [(source_station, line_idx) for line_idx in station_to_lines[source_station]]
    dest_nodes = [(dest_station, line_idx) for line_idx in station_to_lines[dest_station]]

    for source_node in source_nodes:
        for dest_node in dest_nodes:
            try:
                path = nx.dijkstra_path(G, source_node, dest_node, weight='weight')
                total_time = 0
                current_line = path[0][1]

                # Determine the first action
                if path[0][0] == source_station:
                    if path[1][0] == source_station:
                        # First action is a transfer
                        #print(f"Starting with a transfer from line {current_line} to line {path[1][1]} at station {source_station}")
                        pass
                    else:
                        # First action is traveling on the same line
                        total_time += waiting[current_line]
                        #print(f"At station {source_station}, waiting time for line {current_line}: {waiting[current_line]} seconds")

                # Traverse the path
                for i in range(len(path) - 1):
                    u = path[i]
                    v = path[i + 1]
                    edge_weight = G[u][v]['weight']
                    next_line = v[1]
                    '''
                    if u[0] == v[0] and current_line != next_line:
                        # Transfer at the same station (not at starting station)
                        print(f"Transfer from line {current_line} to line {next_line} at station {u[0]}")
                        print(f"  Transfer time + waiting time: {edge_weight} seconds")
                    else:
                        # Travel between stations
                        print(f"Travel from station {u[0]} to station {v[0]} on line {current_line}")
                        print(f"  Travel time: {edge_weight} seconds")
                    '''
                    total_time += edge_weight
                    current_line = next_line

                #print(f"Total time: {total_time} seconds")
                #print("\n")
                
                if total_time < min_total_time:
                    min_total_time = total_time
                    best_path = path

            except nx.NetworkXNoPath:
                continue

    return min_total_time, best_path


def compute_shortest_time_with_walking(G_with_walking, source_station, dest_station):
    min_total_time = float('inf')
    best_path = None

    source_nodes = [(source_station, line_idx) for line_idx in station_to_lines[source_station]]

    dest_nodes = [(dest_station, line_idx) for line_idx in station_to_lines[dest_station]]

    for source_node in source_nodes:
        for dest_node in dest_nodes:
            try:
                path = nx.dijkstra_path(G_with_walking, source_node, dest_node, weight='weight')
                total_time = 0
                travel_time = 0
                current_line = path[0][1]
                previous_action = None  # To track if the previous action was walking

                # Determine the first action
                if path[0][0] == source_station:
                    if path[1][0] == source_station:
                        # First action is a transfer
                        #print(f"Starting with a transfer from line {current_line} to line {path[1][1]} at station {source_station}")
                        pass
                    elif path[1][0] != source_station and path[1][1] != current_line:
                        # First action is walking
                        #print(f"Starting by walking to station {path[0][0]}")
                        pass
                    else:
                        # First action is traveling on the same line
                        total_time += waiting[current_line]
                        #print(f"At station {source_station}, waiting time for line {current_line}: {waiting[current_line]} seconds")
                else:
                    # Starting by walking, do not add waiting time
                    #print(f"Starting by walking to station {path[0][0]}")
                    pass

                for i in range(len(path) - 1):
                    u = path[i]
                    v = path[i + 1]
                    edge_weight = G_with_walking[u][v]['weight']
                    next_line = v[1]

                    if u[0] == v[0] and current_line != next_line:
                        # Transfer at the same station
                        #print(f"Transfer from line {current_line} to line {next_line} at station {u[0]}")
                        #print(f"  Transfer time + waiting time: {edge_weight} seconds")
                        total_time += edge_weight
                    elif u[0] != v[0]:
                        if u[1] == v[1]:
                            # Travel between stations on the same line
                            #print(f"Travel from station {u[0]} to station {v[0]} on line {current_line}")
                            #print(f"  Travel time: {edge_weight} seconds")
                            total_time += edge_weight
                        else:
                            # Walking between stations
                            #print(f"Walk from station {u[0]} to station {v[0]}")
                            #print(f"  Walking time: {edge_weight} seconds")
                            total_time += edge_weight
                            previous_action = 'walk'
                    else:
                        # Same station and same line (should not happen)
                        pass

                    # After walking, if the next action is boarding a line, add waiting time
                    if previous_action == 'walk' and u[0] != v[0]:
                        if v[1] != current_line:
                            current_line = v[1]
                            wait_time = waiting[current_line]
                            total_time += wait_time
                            #print(f"At station {v[0]}, waiting time for line {current_line}: {wait_time} seconds")
                        previous_action = None
                    else:
                        current_line = next_line

                #print(f"Total time: {total_time} seconds")
                #print("\n")

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
