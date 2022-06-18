import sys


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
    # print(graph)
    depth = {i + 1: int(1e8) for i in range(len(graph))}
    next_to_visit = [1]
    depth[1] = 0
    while next_to_visit:
        node = next_to_visit.pop(0)
        for child in graph[node]:
            if depth[child] > int(1e7):
                next_to_visit.append(child)
                depth[child] = depth[node] + 1
    return depth


# array = [7, 4, 4, 4, 7, 7, 7]
# corrected_main_function(array)
if __name__ == "__main__":
    _ = sys.stdin.readline()
    str_array = sys.stdin.readline()
    array = [int(x) for x in str_array.strip().split()]
    result = list(corrected_main_function(array).values())
    print(" ".join(map(str, result)))
