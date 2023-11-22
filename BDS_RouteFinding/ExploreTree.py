from collections import defaultdict

visited = []
queue = []


def bfs_RFP(graph, s, d):
    visited = []
    queue = [[s]]
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            curr = graph[node]
            for current in curr:
                new_path = list(path)
                new_path.append(current)
                queue.append(new_path)
                count = 0
                if current == d:
                    q = queue[-1]
                    for i in range(len(q) - 1):
                        count = count + 1
                        new_list = q[i:i + 2]
                        # new_list=new_list
                    val = count
                    print(val)
                    for i in range(len(q) - 1):
                        count = count + 1
                        new_list = q[i:i + 2]
                        print(*new_list)

                    return
            visited.append(node)


def bfs(graph, visited, node):
    visited.append(node)
    queue.append(node)

    while queue:
        n = queue.pop(0)
        print(n)

        for curr in graph[n]:
            if curr not in visited:
                visited.append(curr)
                queue.append(curr)


if __name__ == "__main__":
    a = input()
    a = a.split(' ')
    v = int(a[0])
    e = int(a[1])
    arr = []
    n = 2
    for x in range(e):
        numbers = [int(num) for num in input().split(" ", n - 1)]
        arr.append(numbers)
    graph = defaultdict(list)
    for edge in arr:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)

    b = input()
    b = b.split(' ')
    s = int(b[0])
    d = int(b[1])

    bfs_RFP(graph, s, d)
    bfs(graph, visited, s)
