import sys


def make_graph(array):
    graph = {}
    for i, a in enumerate(array):
        if i == 0:
            graph[i + 1] = [2, a]
        elif i == len(array) - 1:
            graph[i + 1] = [i]
        else:
            graph[i + 1] = [i, a, i + 2]
    return graph


## corrected version
def corrected_main_function(array):
    graph = make_graph(array)  # create graph tree
    # print(graph)
    depth = {i + 1: int(1e8) for i in range(len(graph))}
    next_to_visit = [1]
    depth[1] = 0
    while next_to_visit:
        node = next_to_visit.pop(0)
        for child in graph[node]:
            if depth[child] > child + 5:
                next_to_visit.append(child)
                depth[child] = depth[node] + 1
    return depth


ONLINE_JUDGE = __debug__
if ONLINE_JUDGE:
    input = sys.stdin.readline

_ = input()
str_array = input()
array = [int(x) for x in str_array.strip().split()]
result = list(corrected_main_function(array).values())
print(" ".join(map(str, result)))
