# Custom Graph implementation
class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, u, v, weight, is_walking=False):
        if u not in self.graph:
            self.add_node(u)
        if v not in self.graph:
            self.add_node(v)
        self.graph[u][v] = (weight, is_walking)  # Store whether edge is walking
        if not self.directed:
            self.graph[v][u] = (weight, is_walking)

    def get_nodes(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for u in self.graph:
            for v, (weight, is_walking) in self.graph[u].items():
                edges.append((u, v, weight, is_walking))
        return edges

# Modified Dijkstra's algorithm
def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph.graph}
    distances[start] = 0
    previous = {node: None for node in graph.graph}
    edge_types = {node: None for node in graph.graph}  # Track if edge is walking
    unvisited = set(graph.graph.keys())
    
    while unvisited:
        current = min(unvisited, key=lambda node: distances[node])
        if current == end:
            break
        unvisited.remove(current)
        
        for neighbor in graph.graph[current]:
            if neighbor in unvisited:
                weight, is_walking = graph.graph[current][neighbor]
                # Calculate distance based on edge type
                distance = distances[current] + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    edge_types[neighbor] = is_walking
    
    if distances[end] == float('infinity'):
        return None, None, None
        
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    return distances[end], path, edge_types

# Station lists and attributes remain unchanged
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

# Initialize the graphs
G = Graph()
G_with_walking = Graph(directed=True)

# Add nodes and edges for each line separately
for line_idx, line in enumerate(station_list):
    # Create nodes with (station, line)
    for i in range(len(line) - 1):
        u = (line[i], line_idx)
        v = (line[i + 1], line_idx)
        travel_time = traveling[line_idx][i]
        G.add_edge(u, v, travel_time)
        G_with_walking.add_edge(u, v, travel_time)

# Add transfer edges
for station, transfers_at_station in transfer.items():
    for (line_i, line_j), trans_time in transfers_at_station.items():
        u = (station, line_i)
        v = (station, line_j)
        total_transfer_time = trans_time + waiting[line_j]
        G.add_edge(u, v, total_transfer_time)
        G_with_walking.add_edge(u, v, total_transfer_time)

# Update how walking edges are added - simplified
for (station_u, station_v), walk_time in walking.items():
    for line_u in station_to_lines[station_u]:
        for line_v in station_to_lines[station_v]:
            u = (station_u, line_u)
            v = (station_v, line_v)
            # Add just walking time, mark as walking edge
            G_with_walking.add_edge(u, v, walk_time, is_walking=True)

def compute_shortest_time_no_walking(G, source_station, dest_station):
    min_total_time = float('inf')
    best_path = None

    source_nodes = [(source_station, line_idx) for line_idx in station_to_lines[source_station]]
    dest_nodes = [(dest_station, line_idx) for line_idx in station_to_lines[dest_station]]

    for source_node in source_nodes:
        for dest_node in dest_nodes:
            time, path, _ = dijkstra(G, source_node, dest_node)
            if path:
                total_time = time
                if path[0][1] == path[1][1]:
                    total_time += waiting[path[0][1]]
                if total_time < min_total_time:
                    min_total_time = total_time
                    best_path = path

    return min_total_time, best_path

def compute_shortest_time_with_walking(G, source_station, dest_station, verbose=True):
    min_total_time = float('inf')
    best_path = None
    best_edge_types = None

    source_nodes = [(source_station, line_idx) for line_idx in station_to_lines[source_station]]
    dest_nodes = [(dest_station, line_idx) for line_idx in station_to_lines[dest_station]]

    for source_node in source_nodes:
        for dest_node in dest_nodes:
            time, path, edge_types = dijkstra(G, source_node, dest_node)
            if path:
                total_time = time
                
                # Process path to add waiting times correctly
                for i in range(len(path)-1):
                    current = path[i]
                    next_node = path[i+1]
                    
                    # Get the edge type (walking or not) between current and next node
                    is_walking = G.graph[current][next_node][1]
                    
                    # Add waiting time only when:
                    # 1. It's the first node and we're starting on a line
                    # 2. We just finished walking and are starting a new line segment
                    if (i == 0 and not is_walking) or (i > 0 and edge_types[path[i-1]] and not is_walking):
                        total_time += waiting[current[1]]
                
                if total_time < min_total_time:
                    min_total_time = total_time
                    best_path = path
                    best_edge_types = edge_types

    if best_path and verbose:
        formatted_path = []
        for i, node in enumerate(best_path):
            if i < len(best_path) - 1:
                is_walking = G.graph[node][best_path[i+1]][1]
                formatted_path.append(f"Station {node[0]} on Line {node[1]} {'(Walking)' if is_walking else ''}")
            else:
                formatted_path.append(f"Station {node[0]} on Line {node[1]}")
        return min_total_time, formatted_path
    return min_total_time if best_path else None, best_path

# Example usage
source_station = 0  # S0
dest_station = 21   # S22

print(f"Source station: {source_station}, Destination station: {dest_station}\n")
min_time_no_walking, path_no_walking = compute_shortest_time_no_walking(G, source_station, dest_station)
print(f"Minimum total time without walking: {min_time_no_walking} seconds\n")

min_time_with_walking, path_with_walking = compute_shortest_time_with_walking(G_with_walking, source_station, dest_station)
print(f"Minimum total time with walking: {min_time_with_walking} seconds\n")

print("Difference in time between the two paths is", min_time_no_walking - min_time_with_walking)