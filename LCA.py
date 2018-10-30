
class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def find_path(self, start_vertex, end_vertex, path=None):
        """ find a path from start_vertex to end_vertex
            in graph """
        if path == None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex,
                                               end_vertex,
                                               path)
                if extended_path:
                    return extended_path
        return []

    def findAllPaths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to
            end_vertex in graph """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.findAllPaths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

    # finds the depth of the longest path between node and root
    def findDepth(self, root, node):
        paths = self.findAllPaths(root, node)
        if (paths == []):
            return -1
        maxDepth = 0
        for path in paths:
            if (len(path) -1 > maxDepth):
                maxDepth = len(path) - 1
        return maxDepth


    # Returns LCA if node n1 , n2 are present in the given
    # DAG otherwise return -1
    def findLCA(self, root, n1, n2):
        # To store paths to n1 and n2 from the root
        paths1 = self.findAllPaths(root, n1)
        paths2 = self.findAllPaths(root, n2)

        # Find paths from root to n1 and root to n2.
        # If either n1 or n2 is not present , return -1
        if (paths1 == [] or paths2 == []):
            return -1

        # Compare the paths to get the first different value
        lca = root
        depth = 0
        for path1 in paths1:
            for path2 in paths2:
                i = 0
                while (i < len(path1) and i < len(path2)):
                    if path1[i] != path2[i]:
                        break
                    i += 1
                if (self.findDepth(root,path1[i-1]) > depth):
                    lca = path1[i-1]
        return lca
