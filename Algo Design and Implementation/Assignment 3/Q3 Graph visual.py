from os import walk
from matplotlib.offsetbox import OffsetBox
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

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

# Map stations to lines
station_to_lines = {}
for line_idx, line in enumerate(station_list):
    for station in line:
        if station not in station_to_lines:
            station_to_lines[station] = []
        station_to_lines[station].append(line_idx)

def get_travel_time(line_idx, station_idx):
    return traveling[line_idx][station_idx]

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
        # Edge weight is just the travel time (wait time already considered at the transfer edges)
        edge_weight = travel_time
        G.add_edge(u, v, weight=edge_weight)

# Add transfer edges between lines at the same station
for station, lines_at_station in station_to_lines.items():
    lines = list(lines_at_station)
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                line_i = lines[i]
                line_j = lines[j]
                # Get transfer time
                transfer_time = transfer.get(station, {}).get((line_i, line_j))
                if transfer_time is None:
                    transfer_time = transfer.get(station, {}).get((line_j, line_i), 0)
                # Include waiting time for the new line
                wait_time_line_j = waiting[line_j]
                edge_weight = transfer_time + wait_time_line_j
                u = (station, line_i)
                v = (station, line_j)
                G.add_edge(u, v, weight=edge_weight)

'''
walking graph
'''

G_with_walking = nx.DiGraph()

# Add edges for traveling on the same line
for line_idx, line in enumerate(station_list):
    for i in range(len(line)):
        station = line[i]
        node = (station, line_idx)
        G_with_walking.add_node(node)
        
        if i < len(line) - 1:
            next_station = line[i + 1]
            next_node = (next_station, line_idx)
            travel_time = get_travel_time(line_idx, i)  # Travel time between station and next_station
            # Add edge for traveling to the next station on the same line
            G_with_walking.add_edge(node, next_node, weight=travel_time)

# Add edges for transfers at the same station
for station, transfers_at_station in transfer.items():
    for (line_i, line_j), trans_time in transfers_at_station.items():
        node_i = (station, line_i)
        node_j = (station, line_j)
        if G_with_walking.has_node(node_i) and G_with_walking.has_node(node_j):
            # Transfer edge includes transfer time and waiting time on the new line
            total_transfer_time = trans_time + waiting[line_j]
            G_with_walking.add_edge(node_i, node_j, weight=total_transfer_time)

# Add edges for walking between stations
for (station_u, station_v), walk_time in walking.items():
    # Connect all line combinations for station_u to station_v
    for line_u in station_to_lines[station_u]:
        for line_v in station_to_lines[station_v]:
            node_u = (station_u, line_u)
            node_v = (station_v, line_v)
            if G_with_walking.has_node(node_u) and G_with_walking.has_node(node_v):
                # Walking edge includes walking time and waiting time on the new line
                total_walk_time = walk_time + waiting[line_v]
                G_with_walking.add_edge(node_u, node_v, weight=total_walk_time)


'''
Computations
'''

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

# Function to compute shortest time with walking
def compute_shortest_time_with_walking(G, source_station, dest_station, verbose=True):
    
    min_total_time = float('inf')
    best_path = None

    # Generate all possible source and destination nodes based on lines
    source_nodes = [(source_station, line_idx) for line_idx in station_to_lines[source_station]]
    dest_nodes = [(dest_station, line_idx) for line_idx in station_to_lines[dest_station]]

    # Iterate through all combinations of source and destination nodes
    for source_node in source_nodes:
        for dest_node in dest_nodes:
            try:
                # Compute the shortest path based on edge weights
                path = nx.dijkstra_path(G, source_node, dest_node, weight='weight')
                # Compute the total time for this path
                total_time = nx.dijkstra_path_length(G, source_node, dest_node, weight='weight')
                
                if path[0][1] == path[1][1]:
                    # If the source and destination are on the same line, no walking is needed
                    total_time += waiting[path[0][1]]    
                
                if verbose:
                    print(f"Evaluating path: {path} with total time: {total_time} seconds")               
                
                # Update the best path if a shorter time is found
                if total_time < min_total_time:
                    min_total_time = total_time
                    best_path = path

            except nx.NetworkXNoPath:
                continue

    if best_path:
        # Calculate total time by summing all edge weights
        total_time = 0
        for i in range(len(best_path) - 1):
            u = best_path[i]
            v = best_path[i + 1]
            edge_weight = G[u][v]['weight']
            total_time += edge_weight
            if verbose:
                action = "Travel" if u[1] == v[1] else "Walk/Transfer"
                print(f"{action} from {u} to {v}: {edge_weight} seconds")

        # Determine if the first action is traveling or walking
        first_u = best_path[0]
        first_v = best_path[1]
        if first_u[1] == first_v[1]:
            # First action is traveling on the same line, add initial wait
            initial_wait = waiting[first_u[1]]
            total_time += initial_wait
            if verbose:
                print(f"Initial waiting time at {first_u}: {initial_wait} seconds")
        elif(first_u[0] == first_v[0]):
            # the only move is walking, you subtract the waiting time at the end station
            total_time -= waiting[first_v[1]]
        else:
            # First action is walking, waiting time is already included in the walking edge
            if verbose:
                print(f"No initial waiting time added as first step is walking from {first_u} to {first_v}")

        # Format the path
        formatted_path = []
        for node in best_path:
            station, line = node
            formatted_path.append(f"Station {station} on Line {line}")

        return total_time, formatted_path
    else:
        if verbose:
            print("No path found")
        return None, None

# Example usage of the compute_shortest_time function
source_station = 0  # S0
dest_station = 20   # S22

print(f"Source station: {source_station}, Destination station: {dest_station}\n")
min_time_no_walking, path_no_walking = compute_shortest_time_no_walking(G, source_station, dest_station)
print(f"Minimum total time without walking: {min_time_no_walking} seconds\n")

min_time_with_walking, path_with_walking = compute_shortest_time_with_walking(G_with_walking, source_station, dest_station)
print(f"Minimum total time with walking: {min_time_with_walking} seconds\n")

print("Difference in time between the two paths is", min_time_no_walking - min_time_with_walking)


'''
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

# Print the difference_in_times matrix without .0
for i in range(n_stations):
    print(' '.join([str(int(j)) for j in difference_in_times[i]]))
'''
'''
def visualize_graph(G, station_to_lines, transfer_stations, walking_edges):
    pos = nx.spring_layout(G, k=0.5, iterations=300)  # Layout for the graph with more spacing
    colors = ['r', 'g', 'b', 'c', 'm', 'y']  # Colors for different lines

    # Draw nodes and edges for each line
    for line_idx, line in enumerate(station_list):
        line_nodes = [(station, line_idx) for station in line]
        nx.draw_networkx_nodes(G, pos, nodelist=line_nodes, node_color=colors[line_idx % len(colors)], node_shape='o', label=f'Line {line_idx}')
        edges = [((line[i], line_idx), (line[i + 1], line_idx)) for i in range(len(line) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=colors[line_idx % len(colors)])

    # Highlight transfer stations with a different shape
    transfer_nodes = [(station, line_idx) for station in transfer_stations for line_idx in station_to_lines[station]]
    nx.draw_networkx_nodes(G, pos, nodelist=transfer_nodes, node_size=100, label='Transfer Station')

    # Draw walking edges with bolder lines
    nx.draw_networkx_edges(G, pos, edgelist=walking_edges, edge_color='k', width=2.0, style='dashed', label='Walking Path')

    # Draw labels
    labels = {node: node[0] for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels)

    # Draw edge labels for travel times
    edge_labels = {(u, v): f"{data['weight']}" for u, v, data in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.legend()
    plt.show()


# Visualize the graph
walking_edges = [((u, line_u), (v, line_v)) for (u, v), walk_time in walking.items() for line_u in station_to_lines[u] for line_v in station_to_lines[v]]
transfer_stations = [station for station, lines in station_to_lines.items() if len(lines) > 1]
visualize_graph(G_with_walking, station_to_lines, transfer_stations, walking_edges)
'''