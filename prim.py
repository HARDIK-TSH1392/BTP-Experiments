class Graph:
    def __init__(self):
        self.edge = []
        self.vertex = []
        self.vertex_num = 0

    def add_node(self, node):
        if node not in self.vertex:
            self.vertex.append(node)
            self.vertex_num += 1

    def add_edge(self, vertex1, vertex2, weight):
        self.edge.append([vertex1, vertex2, weight])

    def prim(self):
        mst = {}
        visited = []
        edges = self.edge
        visited.append(self.vertex[0])
        while len(visited) < self.vertex_num:
            min_edge = []
            for edge in edges:
                if list(set(edge) & set(visited)) and len(list(set(edge) & set(visited))) < 2:
                    if not min_edge or min_edge[2] > edge[2]:
                        min_edge = edge
            mst[(min_edge[0], min_edge[1])] = min_edge[2]
            if min_edge[0] not in visited:
                visited.append(min_edge[0])
            if min_edge[1] not in visited:
                visited.append(min_edge[1])
            edges.remove(min_edge)

        return mst


for i in range(10000):
    g = Graph()
for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
    g.add_node(node)

    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'I', 8)
    g.add_edge('B', 'I', 11)
    g.add_edge('B', 'C', 8)
    g.add_edge('C', 'D', 7)
    g.add_edge('C', 'F', 4)
    g.add_edge('C', 'H', 2)
    g.add_edge('D', 'E', 9)
    g.add_edge('D', 'F', 3)
    g.add_edge('F', 'E', 10)
    g.add_edge('F', 'G', 2)
    g.add_edge('H', 'G', 6)
    g.add_edge('I', 'H', 7)
    g.add_edge('I', 'G', 1)

    mst = g.prim()
    # print('MST =', mst)
    total_weight = 0
    for w in mst.values():
        total_weight += w
    # print('Total Edge Weight =', total_weight)
