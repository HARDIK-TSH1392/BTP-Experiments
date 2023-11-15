class Graph:
    def __init__(self):
        self.edge = []
        self.vertex = []
        self.vertex_num = 0
        self.indeg = {}

    def add_node(self, node):
        if node not in self.vertex:
            self.vertex.append(node)
            self.vertex_num += 1
            self.indeg[node] = 0

    def add_edge(self, vertex1, vertex2, weight=0):
        self.edge.append([vertex1, vertex2, weight])
        self.indeg[vertex2] += 1

    def remove_edges(self, vertex1, vertex2):
        stack = []
        for edge in self.edge:
            if vertex1 and vertex2:
                if edge[0] == vertex1 and edge[1] == vertex2:
                    stack.append(edge)
                    self.indeg[edge[1]] -= 1
            elif vertex1 and not vertex2:
                if edge[0] == vertex1:
                    stack.append(edge)
                    self.indeg[edge[1]] -= 1
            else:
                if edge[1] == vertex2:
                    stack.append(edge)
                    self.indeg[edge[0]] -= 1
        for item in stack:
            self.edge.remove(item)

    def topologicalSort(self):
        result = []
        for i in range(self.vertex_num):
            for vertex, edge_num in self.indeg.items():
                if edge_num == 0 and vertex not in result:
                    self.remove_edges(vertex, None)
                    result.append(vertex)
        return result


for i in range(10000):
    g = Graph()
    for node in ['A', 'B', 'C', 'D', 'E']:
        g.add_node(node)

    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('A', 'D')
    g.add_edge('A', 'E')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')
    g.add_edge('E', 'B')

    # print(g.topologicalSort())
