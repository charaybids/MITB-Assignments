import networkx as nx
import matplotlib.pyplot as plt

def parse_input():
    with open('A3Q3.in', 'r') as f:
        lines = f.readlines()
    idx = 0
    n, m = map(int, lines[idx].split())
    idx += 1

    G = nx.Graph()

    # Parse MRT lines
    for _ in range(m):
        tokens = lines[idx].split()
        waiting_time = int(tokens[0])
        tokens = tokens[1:]
        stations = []
        travel_times = []
        i = 0
        while i < len(tokens):
            station = tokens[i]
            stations.append(station)
            i += 1
            if i < len(tokens):
                travel_time = int(tokens[i])
                travel_times.append(travel_time)
                i += 1
        # Add edges for train connections
        for j in range(len(stations) - 1):
            G.add_edge(
                stations[j], stations[j+1],
                weight=travel_times[j],
                type='train'
            )
        idx += 1

    # Parse interchange stations
    num_interchanges = int(lines[idx])
    idx += 1
    for _ in range(num_interchanges):
        tokens = lines[idx].split()
        station = tokens[0]
        for transfer_info in tokens[1:]:
            lines_pair, time = transfer_info.rsplit(':', 1)
            time = int(time)
            line_from, line_to = lines_pair.split(':')
            # Add transfer edges (assuming transfer as a self-loop or an edge)
            G.add_edge(
                station + '_' + line_from,
                station + '_' + line_to,
                weight=time,
                type='transfer'
            )
        idx += 1

    # Parse walking paths
    num_walks = int(lines[idx])
    idx += 1
    for _ in range(num_walks):
        tokens = lines[idx].split()
        station_a = tokens[0]
        station_b = tokens[1]
        walk_time = int(tokens[2])
        G.add_edge(
            station_a, station_b,
            weight=walk_time,
            type='walk'
        )
        idx += 1

    return G

def visualize_graph(G):
    pos = nx.spring_layout(G, k=0.3)
    edge_types = nx.get_edge_attributes(G, 'type')

    # Separate edges by type
    train_edges = [(u, v) for u, v, d in G.edges(data=True) if d['type'] == 'train']
    transfer_edges = [(u, v) for u, v, d in G.edges(data=True) if d['type'] == 'transfer']
    walk_edges = [(u, v) for u, v, d in G.edges(data=True) if d['type'] == 'walk']

    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=300, node_color='lightblue')
    nx.draw_networkx_labels(G, pos, font_size=8)

    # Draw edges
    nx.draw_networkx_edges(G, pos, edgelist=train_edges, edge_color='blue')
    nx.draw_networkx_edges(G, pos, edgelist=transfer_edges, edge_color='green', style='dashed')
    nx.draw_networkx_edges(G, pos, edgelist=walk_edges, edge_color='red', style='dotted')

    plt.title('MRT Network Visualization')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    G = parse_input()
    visualize_graph(G)