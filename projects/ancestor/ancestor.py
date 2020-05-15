from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    path = []

    for vertex in range(0,20):
        g.add_vertex(vertex)
    for i in ancestors:
        g.add_edge(i[0], i[1])
    for vertex in g.vertices:
        if g.dfs(vertex, starting_node) is not None and len(g.dfs(vertex, starting_node)) > 0:
            path.append(g.dfs(vertex, starting_node))
    if len(path) == 1:
        return -1

    start_path = path[0]
    for i in path:
        if len(i) > len(start_path) or len(i) == len(start_path) and i[0] < start_path[0]:
            start_path = i
    return start_path[0]