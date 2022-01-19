from collections import defaultdict
import argparse


class Graph:

    # Default dict to store Graph
    def __init__(self):

        self.graph = defaultdict(list)
        self.edges = {}
        self.prev_vertex = {}

# adding an Edge
    def add_edge(self, u, v, weight=1):

        self.graph[u].append(v)
        self.graph[v].append(u)

        self.edges[(u, v)] = weight
        self.edges[(v, u)] = weight

# Checking path exist or not between nodes using BFS.
    def isConnected(self, u, v):

        visted = {}
        for i in self.graph:
            visted[i] = False

        queue = []
        queue.append(u)
        connected_vertices = set()

        while queue:
            temp = queue.pop(0)
            connected_vertices.add(temp)
            visted[temp] = True
            for i in self.graph[temp]:
                if (visted[i] is False):
                    queue.append(i)

        if u in connected_vertices and v in connected_vertices:
            return True
        return False

# Find the shortest path using Dijkstra algorithm.
    def Dijkstra(self, node):
        dist = {}
        vetx = {}
        for i in self.graph:
            if i == node:
                dist[(node, i)] = 0
            else:
                dist[(node, i)] = 10**9
        for i in self.graph:
            vetx[i] = False
        temp = node
        while vetx[temp] is False:
            vetx[temp] = True
            for i in self.graph[temp]:
                if (vetx[i] is False
                    and dist[(node, i)] > self.edges[(temp, i)]
                        + dist[(node, temp)]):
                    dist[(node, i)] = self.edges[(temp, i)]
                    + dist[(node, temp)]
                    self.prev_vertex[i] = temp
            temp_dict = {}
            for i in self.graph[temp]:
                temp_dict[i] = dist[(node, i)]
            temp_dict = sorted(temp_dict.items(),
                               key=lambda kv: (kv[1], kv[0]))
            for i in range(len(temp_dict)):
                if vetx[temp_dict[i][0]] is False:
                    temp = temp_dict[i][0]
                    break
            else:
                if vetx[self.prev_vertex[temp]] is False:
                    temp = self.prev_vertex[temp]
                else:
                    min_dist = 10**9
                    for i in self.graph:
                        if vetx[i] is False and dist[(node, i)] < min_dist:
                            temp = i
                            break
        return self.prev_vertex

# Finding previous vertexset from source to destination

    def src_to_dest(self, u, v):

        if self.isConnected(u, v) is True:

            prev_vertex = self.Dijkstra(u)
            prev_vertex = list(prev_vertex.items())
            size = len(prev_vertex)
            src_to_dest = []
            temp = v

            while temp:
                src_to_dest.insert(0, temp)
                if temp == u:
                    break
                for i in range(size):
                    if prev_vertex[i][0] == temp:
                        temp = prev_vertex[i][1]

            src_to_dest = set(src_to_dest)

            return src_to_dest
        else:
            return -1


#  adding arguemets for input and output files
g = Graph()

pars = argparse.ArgumentParser()
pars.add_argument('ip_file', help='Input File')
pars.add_argument('op_file', help='Output File')
pars.add_argument('--s', '--sourece', help='add destination')
pars.add_argument('--d', '--destination', help='add source')
arg = pars.parse_args()


file = open(arg.ip_file, 'r')
file1 = open(arg.op_file, 'w')
# getting input from inputfile.txt
inArr = []

for data in file:
    [x.strip('\n') for x in data]
    inArr.append([int(x) for x in data.split()])

file = open(arg.ip_file, 'r')
file1 = open(arg.op_file, 'w')

order = len(inArr)

# Adding edges Between the conneted nodes

for i in range(len(inArr)):
    for j in range(len(inArr[0])):
        if j-1 >= 0 and inArr[i][j-1] == 1 and inArr[i][j] == 1:
            g.add_edge((i, j-1), (i, j))
        if i-1 >= 0 and inArr[i-1][j] == 1 and inArr[i][j] == 1:
            g.add_edge((i-1, j), (i, j))

a = arg.s
b = arg.d
if a is None:
    a = (0, 0)
else:
    a = tuple(map(int, a.split(',')))
if b is None:
    b = (len(inArr)-1, len(inArr[0])-1)
else:
    b = tuple(map(int, b.split(',')))


temp_list = g.src_to_dest(a, b)

output_list = [[0 for i in range(len(inArr[0]))] for j in range(len(inArr))]

# Representing the set output obtained from
# source to destination function in matrix form

if temp_list == -1:
    output = -1
    file1.write(f' {int(output)} ')
else:
    if type(temp_list) is set:

        for i in range(len(inArr)):
            for j in range(len(inArr[0])):
                if (i, j) in temp_list:
                    output_list[i][j] = int(1)
                else:
                    output_list[i][j] = int(0)

        for i in output_list:
            for j in i:
                file1.write(f' {str(j)} ')
            file1.write('\n')