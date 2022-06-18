def unique(a: int, b: int) -> list[int]:
    if a == b:
        return [a]
    else:
        return [a, b]


def make_graph(array: list[int]) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {}
    for i, a in enumerate(array):
        if i == 0:
            graph[i + 1] = [2, a]
        elif i == len(array) - 1:
            graph[i + 1] = [i]
        else:
            graph[i + 1] = [i, a, i + 2]
    return graph


## corrected version
def corrected_main_function(array: list[int]) -> dict[int, int]:
    graph = make_graph(array)  # create graph tree
    print(graph)
    depth = {}
    next_to_visit = [1]
    depth[1] = 0
    while next_to_visit:
        node = next_to_visit.pop(0)
        for child in graph[node]:
            if child not in depth.keys():
                next_to_visit.append(child)
                depth[child] = depth[node] + 1
    return depth


array = [7, 4, 4, 4, 7, 7, 7]
corrected_main_function(array)
