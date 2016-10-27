class FloydWarshall(object):

    def __init__(self, file_):
        nodes = file_.read().splitlines()
        file_.close()
        self.get_graph(nodes)
        self.len_ = len(self.nodes)
        self.create_fw_matrix()

    def get_graph(self, nodes):
        self.nodes = []
        self.graph = {}
        for node in nodes[1:]:
            [k, v] = node.split()
            if k in self.graph.keys():
                self.graph[k].append(v)
            else:
                self.graph[k] = [v]
                if k not in self.nodes:
                    self.nodes.append(k)
            if v not in self.nodes:
                self.nodes.append(v)

    def create_fw_matrix(self):
        m = [[float('inf')] * self.len_ for i in range(self.len_)]
        for i, x in enumerate(self.nodes):
            for j, y in enumerate(self.nodes):
                if x == y:
                    m[i][j] = 0
                else:
                    if x in self.graph.keys() and y in self.graph[x]:
                        m[i][j] = m[j][i] = 1
        for k in range(self.len_):
            for i in range(self.len_):
                for j in range(self.len_):
                    m[i][j] = min(m[i][j], m[i][k] + m[k][j])
        self.matrix = m
        
    def print_matrix(self):
        for row in self.matrix:
            print (row)
