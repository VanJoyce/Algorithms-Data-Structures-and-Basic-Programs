"""
Vanessa Joyce Tan
30556864
Assignment 4
"""
from math import inf


class MinHeap:
    """
    Class representing a min-heap for graphs.
    """
    def __init__(self, graph, root):
        """
        Creates a min-heap with the vertices in graph with the given root.

        :param graph: the graph with the vertices to be inserted into the min-heap
        :param root: vertex ID of the vertex to be made root of the min-heap
        :pre-condition: vertex IDs in the graph must be consecutive integers starting from 0.
        :post-condition: a min-heap is created with the given root and an index array for mapping which index the vertex
                         is at in the min_heap.

        Assuming V is the number of vertices in graph,
        :time complexity: best case and worst case are both O(V) because have to loop through each vertex in graph to
                          initialize and populate the heap and index mapping array no matter what.
        :space complexity: best case is O(V) and worst case is O(V^2) because space depends on the parameter graph and
                           how dense it is
        :aux space complexity: O(V) because heap and index mapping array only depends on the vertices in the graph
        """
        self.heap = [None, None]
        self.index = []
        ind = 2
        for vertex in graph.vertices:
            if vertex.id == root:
                self.heap[1] = (vertex, 0)
                self.index.append(1)
            else:
                self.heap.append((vertex, inf))
                self.index.append(ind)
                ind += 1
        self.last = len(self.heap) - 1

    def rise(self, vertex_id):
        """
        Rises the element in the heap which contains the vertex with the given ID until either its distance is no longer
        smaller than its parent or it has reached the root.

        :param vertex_id: ID of the vertex which we want to rise
        :pre-condition: vertex_id must be an integer from 0 to length of index mapping array
        :post-condition: the current element with the minimum distance is at the root of the min-heap.

        Assuming V is the number of vertices in the min-heap,
        :time complexity: best and worst case are both O(log V) because it can only swap with its parent which we get
                          its index by integer dividing the child's current index by 2. Swapping also only takes O(1)
        :space complexity: O(1) because the function doesn't store anything. It just checks some conditions and swap
        :aux space complexity: O(1)
        """
        i = self.index[vertex_id]
        child = self.heap[i]
        if i > 1:   # if the vertex is not at root
            parent_ind = i // 2
            parent = self.heap[parent_ind]

            # keep rising until the distance is not shorter than parent's or it is already at root
            while parent is not None and child[1] < parent[1]:
                self.swap(child, parent)
                i = self.index[child[0].id]
                parent_ind = i // 2
                parent = self.heap[parent_ind]

    def sink(self, vertex_id):
        """
        Sinks the element in the heap which contains the vertex with the given ID until either its distance is no longer
        bigger than its children or it has no more children.

        :param vertex_id: ID of the vertex which we want to sink
        :pre-condition: vertex_id must be an integer from 0 to length of index mapping array
        :post-condition: the current element with the minimum distance is at the root of the min-heap.

        Assuming V is the number of vertices in the min-heap,
        :time complexity: best and worst case are both O(log V) because it can only swap with its children which we get
                          its index by multiplying the current index by 2 (and add 1 for right child). Swapping also
                          only takes O(1).
        :space complexity: O(1) because the function doesn't store anything. It just checks some conditions and swap
        :aux space complexity: O(1)
        """
        i = self.index[vertex_id]
        parent = self.heap[i]

        left = None
        if i*2 < self.last:
            left = self.heap[i * 2]

        right = None
        if i * 2 + 1 < self.last:
            right = self.heap[i * 2 + 1]

        # keep sinking if there are children that are smaller than parent
        while (left is not None and parent[1] > left[1]) or (right is not None and parent[1] > right[1]):
            if left is not None and right is not None:
                if right[1] < left[1]:
                    self.swap(parent, right)
                else:
                    self.swap(parent, left)
            elif right is None:
                self.swap(parent, left)
            elif left is None:
                self.swap(parent, right)

            i = self.index[parent[0].id]
            parent = self.heap[i]

            left = None
            if i * 2 < self.last:
                left = self.heap[i * 2]

            right = None
            if i * 2 + 1 < self.last:
                right = self.heap[i * 2 + 1]

    def serve(self):
        """
        Serves the root of the min-heap by swapping with the last element of the min-heap and making it finalized.

        :return: the element of the min-heap which has the minimum distance
        :pre-condition: -
        :post-condition: the current element with the minimum distance is at the root of the min-heap.

        Assuming V is the number of vertices in the min-heap,
        :time complexity: best and worst case are both O(log V) because it sinks the root after the swap.
        :space complexity: O(1) because the function doesn't store anything. It just checks some conditions and swap
        :aux space complexity: O(1)
        """
        pair = self.heap[1]
        last_pair = self.heap[self.last]
        self.swap(pair, last_pair)

        vertex = pair[0]
        vertex.finalized = True
        self.last -= 1
        self.sink(self.heap[1][0].id)
        return pair

    def relax_edge(self, edge):
        """
        Performs edge relaxation for given edge.

        :param edge: an edge between vertices which contains the IDs of the vertices on both ends and the weight
        :pre-condition: edge must contain the IDs of the vertices on both ends and the weight
        :post-condition: the vertices that are not finalized will have their predecessor and distances updated so that
                         it stores the shortest distance of itself from the source so far. The current element with the
                         minimum distance is at the root of the min-heap.

        Assuming V is the number of vertices in the min-heap,
        :time complexity: best and worst case are both O(log V) because it rises the vertex which is not finalized.
        :space complexity: O(1) because the function doesn't store anything. It just updates distance and predecessor.
        :aux space complexity: O(1)
        """
        i = self.index[edge.u]
        j = self.index[edge.v]

        predecessor = self.heap[i]
        current = self.heap[j]
        if not current[0].finalized:
            current[0].predecessor = edge.u
            new_distance = predecessor[1] + edge.w
            if new_distance < current[1]:
                self.heap[j] = (current[0], new_distance)
            self.rise(current[0].id)

    def swap(self, first, second):
        """
        Swaps two elements in the heap and index mapping array.

        :param first: the first element of min-heap to be swapped
        :param second: the second element of min-heap to be swapped
        :pre-condition: parameters first and second must be tuples where the first item is a Vertex object and second
                        item is the distance.
        :post-condition: the tuples given are swapped in the min_heap and their index mapping array is updated

        :time complexity: best and worst case is O(1) because no need to compute anything, just swap
        :space complexity: O(1) because it doesn't store anything
        :aux space complexity: O(1)
        """
        i = first[0].id
        j = second[0].id
        m = self.index[i]
        n = self.index[j]
        self.index[i], self.index[j] = self.index[j], self.index[i]
        self.heap[m], self.heap[n] = self.heap[n], self.heap[m]


class Edge:
    """
    Class that represents an edge between vertices in a graph.
    """

    def __init__(self, u, v, w):
        """
        Creates an edge between two vertices, u and v.

        :param u: ID of the source vertex
        :param v: ID of the destination vertex
        :param w: weight of the edge

        :time complexity: best case and worst case are both O(1) because each edge will store the same amount of info
        :space complexity: O(1) because all edges take the same amount of space
        :aux space complexity: O(1)
        """
        self.u = u
        self.v = v
        self.w = w


class Vertex:
    """
    Class that represents a vertex in a graph.
    """

    def __init__(self, id):
        """
        Creates a vertex with a list of edges.

        :param id: an integer used as identification of the vertex

        :time complexity: best case and worst case are both O(1) because it takes the same amount of time to create any
                          vertex
        :space complexity: O(1) because each vertex takes up the same amount of space when created since its list of
                           edges are empty
        :aux space complexity: O(1)
        """
        self.id = id
        self.edges = []
        self.finalized = False
        self.predecessor = None

    def add_edge(self, u, v, w):
        """
        Creates an edge between two vertices, u and v.

        :param u: ID of the source vertex
        :param v: ID of the destination vertex
        :param w: the weight of the edge

        :time complexity: best and worst case in O(1) because it appends an Edge object to the edge list no matter what
        :space complexity: O(1) because it is just appending to the back of edge list
        :aux space complexity: O(1)
        """
        self.edges.append(Edge(u, v, w))


class Graph:
    """
    Class that represents a graph.
    """

    def __init__(self, gfile):
        """
        Creates a connected, undirected and simple graph based on a given text file.

        :param gfile: the text file containing the information about the graph
        :pre-condition: the first line of gfile is the number of vertices in the graph,
                        the rest of the lines must have three integers separated by spaces which represents and edge
                        (the first two integers are the vertex IDs and the third integer is the non-negative weight)
        :post-condition: a graph which is connected, undirected and simple is created represented by an adjacency list

        Assuming V is the number of vertices in the graph,
        :time complexity: best case is O(V) because there must at least be (V-1) edges in a simple, connected and
                          undirected graph
                          worst case is O(V^2) because the maximum number of edges in a simple, connected and
                          undirected graph is V(V-1)/2 so we would need to process that many number of lines in the
                          file.
        :space complexity: best case is O(V) when there are the minimum number of edges in a simple, connected and
                           undirected graph (which is when each vertex stores minimum one edge and at most two edges)
                           worst case is O(V^2) when each vertex has an edge to every other vertex.
        :aux space complexity: best case is O(V) and worst case is O(V^2)
        """
        file = open(gfile, "r")

        n = int(file.readline())
        self.vertices = []
        for v in range(n):
            self.vertices.append(Vertex(v))

        for line in file:
            edge = line.split()
            u = int(edge[0])
            v = int(edge[1])
            w = int(edge[2])

            # add edges for vertices on both ends of the edge because undirected
            self.add_edge(u, v, w)
            self.add_edge(v, u, w)
        file.close()

    def add_edge(self, u, v, w):
        """
        Adds an edge to the list of edges of vertex u.

        :param u: ID of the source vertex
        :param v: ID of the destination vertex
        :param w: the weight of the edge

        :time complexity: best and worst case in O(1) because it appends an Edge object to the edge list
        :space complexity: O(1) because it is just appending to the back of edge list
        :aux space complexity: O(1)
        """
        self.vertices[u].add_edge(u, v, w)

    def shallowest_spanning_tree(self):
        """
        Finds the shallowest spanning tree of a graph.

        :return: a tuple where the first item is the vertex ID of the root which gives the shallowest spanning tree and
                 the second item is an integer representing its height.
        :pre-condition: -
        :post-condition: -

        Assuming V is the number of vertices in the graph,
        :time complexity: best and worst case are both O(V^3) because in FLoyd-Warshall's algorithm it takes O(V^3) time
                          to populate the matrix no matter what.
        :space complexity: best and worst case are both O(V^2) because we have to make a matrix of size V x V no matter
                           what.
        :aux space complexity: O(V^2)
        """
        matrix = []
        for i in range(len(self.vertices)):
            matrix.append([inf] * len(self.vertices))

        for u in range(len(self.vertices)):
            matrix[u][u] = 0    # distance to itself is 0
            for edge in self.vertices[u].edges:
                v = edge.v
                matrix[u][v] = 1     # if connected, then they have a height of one.

        for j in range(len(self.vertices)):
            for i in range(len(self.vertices)):
                for k in range(len(self.vertices)):
                    if matrix[i][k] > matrix[i][j] + matrix[j][k]:
                        matrix[i][k] = matrix[i][j] + matrix[j][k]

        # process through each row/vertex
        min_height = inf
        root = None
        for i in range(len(matrix)):
            height = 0
            for j in range(len(matrix)):
                if matrix[i][j] > height:
                    height = matrix[i][j]
            if height < min_height:
                min_height = height
                root = i

        return root, min_height

    def shortest_errand(self, home, destination, ice_locs, ice_cream_locs):
        """
        Finds the shortest distance from home to destination while picking up ice and ice cream. Ice has to be picked up
        before the ice cream.

        :param home: integer representing vertex ID of starting point
        :param destination: integer representing vertex ID of destination
        :param ice_locs: a list of one or more vertex IDs of the locations that have ice
        :param ice_cream_locs: a list of one or more vertex IDs of the locations that have ice cream
        :return: a tuple where the first item is the length of the shortest walk and the second item is a list of
                 vertices representing the walk.
        :pre-condition: vertex IDs must be integers
        :post-condition: first vertex in the walk is home. Last vertex in the walk is destination. There is at least one
                         vertex from ice_locs and one vertex from ice_cream_locs in the walk. The vertex from
                         ice_cream_locs appears in the same position or after a vertex from ice_locs.

        Assuming E is the number of edges in the graph and V is the number of vertices in the graph,
        :time complexity: best and worst case are both (E log V) because we have to perform edge relaxation for each
                          edge which costs O(log V).
        :space complexity: best case is O(V) and worst case is O(V^2), depending on how dense the graph is because the
                           min-heap initialized also depends on the size of the graph.
        :aux space complexity: best case is O(V) and worst case is O(V^2)
        """
        # pre-processing: build layers of graph
        ori_len = len(self.vertices)
        for i in range(1, 3):
            for v in range(ori_len):
                new_u = v + (ori_len * i)
                self.vertices.append(Vertex(new_u))

            for v in range(ori_len):
                vertex = self.vertices[v]
                for edge in vertex.edges:
                    new_u = v + (ori_len * i)
                    new_v = edge.v + (ori_len * i)
                    if new_v < ori_len * 3:     # to avoid adding the ice_locs edges which were added in second layer
                        self.add_edge(new_u, new_v, edge.w)

            if i == 1:  # second layer of graph link with original through ice_locs
                for ice in ice_locs:
                    new_ice = ice + (ori_len * i)
                    self.add_edge(ice, new_ice, 0)
                    self.add_edge(new_ice, ice, 0)
            else:       # third layer of graph link with second layer of graph through ice_cream_locs
                for ic in ice_cream_locs:
                    second_ic = ic + ori_len    # vertex ID of ic from second layer
                    new_ic = ic + (ori_len * i)
                    self.add_edge(second_ic, new_ic, 0)
                    self.add_edge(new_ic, second_ic, 0)
        new_destination = destination + (ori_len * 2)

        # Dijkstra
        vertices_heap = MinHeap(self, home)
        current = None
        nearest_distance = 0
        while vertices_heap.last > 0:  # there are still elements which have distances which are not finalized
            vertex, distance = vertices_heap.serve()
            if vertex.id == new_destination:
                current = vertex
                nearest_distance = distance
                break

            # perform edge relaxation for the vertex that has been served
            for edge in vertex.edges:
                vertices_heap.relax_edge(edge)

        backtracking = []
        while current is not None:
            backtracking.append(current.id)
            if current.predecessor is not None:
                current = self.vertices[current.predecessor]
            else:
                current = None

        walk = [home]
        for i in range(len(backtracking)):
            v = backtracking.pop()
            # change the id back to original
            if v >= ori_len * 2:
                v -= ori_len * 2
            elif v >= ori_len:
                v -= ori_len

            if v == walk[-1]: # no repeat vertices
                continue
            else:
                walk.append(v)

        # revert graph back to original state
        while len(self.vertices) > ori_len:
            self.vertices.pop()
        # reset vertices
        for vertex in self.vertices:
            vertex.finalized = False
            vertex.predecessor = None
            if vertex.id in ice_locs:
                vertex.edges.pop()  # pop link to second layer of graph

        return nearest_distance, walk
