import csv
from collections import defaultdict






def read_graph_from_csv(file_name):
        """
        Reads graph data from a CSV file and creates a graph. Each row in the CSV file
        represents an edge with the vertices and their corresponding weight.
        FILES ARE IDENTIFIED IN UNITTEST
        :param file_name: The name of the CSV file to read from.
        :return: A Graph object representing the graph described in the CSV file.
        """
        graph = Graph()
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                well1, well2, distance = row
                graph.add_edge(well1.strip(), well2.strip(), int(distance))
        return graph

class Graph:

    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, source_vertex, destination_vertex, weight):
        """
        Adds an edge between two vertices in the graph with a given weight. This creates
        an undirected graph

        :param source_vertex: The starting vertex of the edge.
        :param destination_vertex: The ending vertex of the edge.
        :param weight: The weight or cost of the edge
        """
        self.graph[source_vertex][destination_vertex] = weight
        self.graph[destination_vertex][source_vertex] = weight

    def prim_alghoritm(self):
        """
        -Starts with any vertex not in visited set from the graph
        -Creates a priority queue for vertices
        -Gets the vertex with and edge that has
        the smallest weight from the queue and deletes it from the queue
        -Adds to visited and to MST
        -Adds vertices that are adjacent to the vertex we've just looked into to the queue
        -REPEAT!

        :return: A list of tuples representing the edges in the MST.
                 Each tuple contains (parent_vertex, current_vertex, weight).
        """
        min_span_tree = []
        visited = set()
        start_vertex = next(iter(self.graph))
        priority_queue = [(0, start_vertex, None)]

        while priority_queue:
            weight, current_vertex, parent = priority_queue.pop(0)

            if current_vertex not in visited:
                min_span_tree.append((parent, current_vertex, weight))
                visited.add(current_vertex)

                for neighbor, edge_weight in self.graph[current_vertex].items():
                    if neighbor not in visited:
                        priority_queue.append((edge_weight, neighbor, current_vertex))
                priority_queue.sort()

        return min_span_tree


def min_cable_length(input_file_name, output_file_name):
    """
    checks if the graph has at least one vertex
    returns -1 (no connected wells)
    else
    uses graph we've created and computes MST
    using a method prim_alghoritm
    then sums all the weights we have in the MST
    returns the results in the file
    FILES ARE IDENTIFIED IN UNITTEST


    :param input_file_name: The name of the input CSV file with graph data.
    :param output_file_name: The name of the output file to write the minimum cable length.
    """
    graph = read_graph_from_csv(input_file_name)
    if not graph.graph:
        min_cable_length = -1
    else:
        mst = graph.prim_alghoritm()
        min_cable_length = sum(weight for _, _, weight in mst)

    with open(output_file_name, "w") as file:
        file.write(str(min_cable_length))