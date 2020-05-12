"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("vertex doesnt exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        todo = Queue()
        todo.enqueue(starting_vertex)
        visited = set()
        while todo.size() > 0:
            cur_vert = todo.dequeue()
            if cur_vert not in visited:
                print(cur_vert)
                visited.add(cur_vert)
                for i in self.get_neighbors(cur_vert):
                    if i not in visited:
                        todo.enqueue(i)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        todo = Stack()
        todo.push(starting_vertex)
        visited = set()
        while todo.size() > 0:
            cur_vert = todo.pop()
            if cur_vert not in visited:
                print(cur_vert)
                visited.add(cur_vert)
                for i in self.get_neighbors(cur_vert):
                    if i not in visited:
                        todo.push(i)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)
        for i in self.get_neighbors(starting_vertex):
            if i not in visited:
                self.dft_recursive(i, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        path = Queue()
        path.enqueue([starting_vertex])
        visited = set()
        while path.size() > 0:
            cur_path = path.dequeue()
            last_visited = cur_path[-1]
            if last_visited not in visited:
                if last_visited == destination_vertex:
                    return cur_path
                else:
                    visited.add(last_visited)
                    neighbors = self.get_neighbors(last_visited)
                    for i in neighbors:
                        cur_path_dup = cur_path[:]
                        cur_path_dup.append(i)
                        path.enqueue(cur_path_dup)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        path = Stack()
        path.push([starting_vertex])
        visited = set()
        while path.size() > 0:
            cur_path = path.pop()
            last_visited = cur_path[-1]
            if last_visited not in visited:
                if last_visited == destination_vertex:
                    return cur_path
                else:
                    visited.add(last_visited)
                    neighbors = self.get_neighbors(last_visited)
                    for i in neighbors:
                        cur_path_dup = cur_path[:]
                        cur_path_dup.append(i)
                        path.push(cur_path_dup)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = list()

        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for i in self.get_neighbors(starting_vertex):
            if i not in visited:
                v_chain = self.dfs_recursive(i, destination_vertex, visited, path)
                if v_chain:
                    return v_chain

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
