import copy
import queue as Q
from queue import PriorityQueue

queue = []


class Graph:
    def __init__(self):
        self.visited = None
        self.graph = dict()
        self.cost_dict = dict()
        self.final_dict = dict()

    def addEdge(self, x, y, weight):
        if x not in self.graph:
            q = Q.PriorityQueue()
            self.graph.update({x: q})
        self.graph[x].put(y)
        self.cost_dict.update({(x, y): weight})

    def node(self):
        self.visited = [False] * 10000

    def UCS_path(self, s, visited, path, goal, value):
        path.append(s)
        visited[s] = True
        if goal == s:
            self.final_dict.update({tuple(path): value})
            return

        for i in self.graph[s].queue:
            if not visited[i]:
                self.UCS_path(i, copy.deepcopy(visited), copy.deepcopy(path), goal, value + self.cost_dict[s, i])
            else:
                return 'none'

    def UCS(self, s, d):
        self.visited[s] = True
        path = [s]
        for i in self.graph[s].queue:
            if not self.visited[i]:
                value = self.cost_dict[s, i]
                self.UCS_path(i, copy.deepcopy(self.visited), copy.deepcopy(path), d, value)

    def shortest_route(self):
        sum = 0
        count = 0
        min_cost = 0
        temp = 10000
        if bool(self.final_dict):

            for i in self.final_dict:
                min_cost = self.final_dict[i]
                count += 1
                if temp > min_cost:
                    temp = min_cost
                # count += 1
        else:
            print("-1")
        print(temp)
        if bool(self.final_dict):
            new_list = min(self.final_dict, key=self.final_dict.get)
            for i in range(len(new_list)):
                sum += 1
            print(sum)
        if bool(self.final_dict):
            new_list = min(self.final_dict, key=self.final_dict.get)
            for i in range(len(new_list)):
                print(*new_list[i:i + 1])

        print(count)


g = Graph()

a = input()
a = a.split(' ')

v = int(a[0])
e = int(a[1])
g.node()
for i in range(0, e):
    a = input()
    a = a.split(' ')
    x = int(a[0])
    y = int(a[1])
    weight = int(a[2])
    g.addEdge(x, y, weight)

a = input()
a = a.split(' ')
s = int(a[0])
d = int(a[1])

g.UCS(s, d)
g.shortest_route()
