import heapq
import os

from decorators import measure_time
from filepaths import DATASET_PATH
from graph_parser import GraphParser
from sample_graph_generator import generate_graph


class SequentialHybrid:
    def __init__(self, graph):
        self.graph = graph
        self.distances = {}

    @measure_time
    def sequential_hybrid(self, source):
        # __init__ialize distances
        self.distances = {vertex: float('inf') for vertex in self.graph}
        self.distances[source] = 0

        # Dijkstra's scan
        i = 0
        while True:
            i += 1
            prev_distances = self.distances.copy()
            self.dijkstra_scan(source)
            if self.distances == prev_distances or i == len(self.graph) - 1:
                break

        # Check for negative cycle
        for u in self.graph:
            for v, weight in self.graph[u].items():
                if self.distances[u] + weight < self.distances[v]:
                    print("There exists a negative cycle")
                    return

        return self.distances

    def dijkstra_scan(self, source):
        q = [(0, source)]
        while q:
            u_dist, u = heapq.heappop(q)
            if u_dist > self.distances[u]:
                continue
            for v, weight in self.graph[u].items():
                alt = self.distances[u] + weight
                if alt < self.distances[v]:
                    self.distances[v] = alt
                    heapq.heappush(q, (alt, v))


if __name__ == "__main__":
    dataset_folder_path = input('Enter path to graph files folder: ') or DATASET_PATH
    files_path = input('Enter name of graph files: ') or 'bay'
    folder_path = os.path.join(dataset_folder_path, files_path)

    parser = GraphParser()
    parsed_graph = parser.parse(folder_path)
    graph = parsed_graph['distance_edges']

    total_edges = sum(len(adjacent_vertices) for adjacent_vertices in graph.values())
    print('number of nodes: ', len(graph), ', number of edges: ', total_edges)
    # print(graph)

    # graph = generate_graph(320000, 790000)
    # print("generated graph: ", graph)

    sequential_hybrid_instance = SequentialHybrid(graph)
    source = int(input('Enter source for graph: ') or '1')  # Set the source node
    distances = sequential_hybrid_instance.sequential_hybrid(source)
    if distances:
        print("Distances:", distances)
