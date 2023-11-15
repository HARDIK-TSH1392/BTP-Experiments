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

    def dijkstra(self, start_vertex, end_vertex):
        data = {}
        result = {}
        visited_node = []
        visited_edge = []
        edges = self.edge
        for v in self.vertex:
            result[v] = [0, []]
            if v != start_vertex:
                data[v] = None
            else:
                data[v] = 0

        current_node = start_vertex
        current_path = []
        current_path.append(start_vertex)
        current_weight = 0

        while len(visited_node) < self.vertex_num:
            min_edge = []
            for edge in edges:
                if current_node in edge and edge not in visited_edge:
                    x = edge[0]
                    y = edge[1]
                    weight = edge[2]
                    if x == current_node:
                        if data[y] is None or data[y] > current_weight + weight:
                            data[y] = current_weight + weight
                            result[y] = [current_weight +
                                         weight, current_path[:]]
                            result[y][1].append(y)

                    else:
                        if data[x] is None or data[x] > current_weight + weight:
                            data[x] = current_weight + weight
                            result[x] = [current_weight +
                                         weight, current_path[:]]
                            result[x][1].append(x)

                    if min_edge == [] or min_edge[2] > weight:
                        min_edge = edge
                    visited_edge.append(edge)

            visited_node.append(current_node)
            if min_edge:
                if min_edge[0] == current_node:
                    current_node = min_edge[1]
                    if not result[min_edge[1]][1]:
                        current_path.append(min_edge[1])
                    else:
                        current_path = result[min_edge[1]][1]
                elif min_edge[1] == current_node:
                    current_node = min_edge[0]
                    if not result[min_edge[1]][1]:
                        current_path.append(min_edge[0])
                    else:
                        current_path = result[min_edge[0]][1]
                current_weight = data[current_node]

        return result[end_vertex]


for i in range(10000):
    g = Graph()
    for node in ['a', 'b', 'c', 'd', 'e', 'f']:
        g.add_node(node)

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', -2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    shortes_path = g.dijkstra('a', 'e')

    # print('path => ', shortes_path[1]) 
    # print('distance =>', shortes_path[0] )