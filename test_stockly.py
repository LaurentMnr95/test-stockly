def unique(a: int, b: int) -> list[int]:
    if a == b:
        return [a]
    else:
        return [a, b]


def make_graph(array: list[int]) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {}
    for i, a in enumerate(array):
        if i == len(array) - 1:
            graph[i + 1] = []
        elif i + 1 == a:
            graph[i + 1] = [i + 2]
        else:
            graph[i + 1] = unique(i + 2, a)
    return graph


def shortcuts(array: list[int]) -> dict[int, int]:
    graph = make_graph(array)
    print(graph)
    visited: set[int] = set()  # Set to keep track of visited nodes of graph.
    depth = {i + 1: 0 for i in range(len(array))}  # dict to store depth
    known_depth: set[int] = set()
    known_depth.add(1)

    def dfs(
        known_depth: set[int], visited: set[int], graph: dict[int, list[int]], node: int
    ):  # function for dfs
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in known_depth:
                    depth[neighbour] = depth[node] + 1
                    known_depth.add(neighbour)
            for neighbour in graph[node]:
                dfs(known_depth, visited, graph, neighbour)

    dfs(known_depth, visited, graph, 1)
    return depth


array = [4, 4, 4, 4, 7, 7, 7]
shortcuts(array)
