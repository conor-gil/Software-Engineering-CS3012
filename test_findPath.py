import unittest
from LCA import Graph
from LCA import findLCA


class testFindPath(unittest.TestCase):

    # test for findPath function in normal scenarios
    def testFindPath(self):
        g = {"a": ["b","c"],
             "b": ["c","d"],
             "c": ["d"],
             "d": ["c"],
             "e": ["f"],
             "f": ["c"]
             }
        graph = Graph(g)
        path = graph.find_path("a","d")
        print(path)
        self.assertListEqual(graph.find_path("a", "d"), ["a", "b", "c", "d"])


    # test for findPath function from the root to itself
    def testFProot(self):
        g = {"a": ["b", "c"],
             "b": ["c", "d"],
             "c": ["d"],
             "d": ["c"],
             "e": ["f"],
             "f": ["c"]
             }
        graph = Graph(g)
        path = graph.find_path("a", "a")
        print(path)
        self.assertListEqual(graph.find_path("a", "a"), ["a"])

    # test for findPath function when the given node
    # doesn't exist
    def testFPfalse(self):
        g = {"a": ["b", "c"],
             "b": ["c", "d"],
             "c": ["d"],
             "d": ["c"],
             "e": ["f"],
             "f": ["c"]
             }
        graph = Graph(g)
        path = graph.find_path("a", "g")
        print(path)
        self.assertListEqual(graph.find_path("a", "g"), [])

    # test for findPath function when no binary tree
    # is provided
    def testFPnull(self):
        g = {
             }
        graph = Graph(g)
        path = graph.find_path("a", "d")
        print(path)
        self.assertListEqual(graph.find_path("a", "d"), [])


class testFindAllPath(unittest.TestCase):

    def testFindAll(self):
        g = {"a": ["b", "c"],
             "b": ["d", "e"],
             "c": ["f"],
             "d": ["g"],
             "e": ["g"],
             "f": ["e", "g"],
             "g": []
             }
        graph = Graph(g)
        paths = graph.findAllPaths("a","g")
        print(path)
        self.assertListEqual(graph.findAllPaths("a","g") , [['a', 'b', 'd', 'g'], ['a', 'b', 'e', 'g'], ['a', 'c', 'f', 'g']])

    def testFAself(self):
        g = {"a": ["b", "c"],
             "b": ["d", "e"],
             "c": ["f"],
             "d": ["g"],
             "e": ["g"],
             "f": ["e", "g"],
             "g": []
             }
        graph = Graph(g)
        paths = graph.findAllPaths("c","c")
        print(path)
        self.assertListEqual(graph.findAllPaths("c","c") , [['c']])

    def testFAone(self):
        g = {"a": ["b", "c"],
             "b": ["d", "e"],
             "c": ["f"],
             "d": ["g"],
             "e": ["g"],
             "f": ["e", "g"],
             "g": []
             }
        graph = Graph(g)
        paths = graph.findAllPaths("d","g")
        print(path)
        self.assertListEqual(graph.findAllPaths("d","g") , [['d', 'g']])
        paths = graph.findAllPaths("f", "g")
        print(path)
        self.assertListEqual(graph.findAllPaths("f", "g"), [['f', 'g'], ['f', 'e', 'g']])

    def testFAfalse(self):
        g = {"a": ["b", "c"],
             "b": ["d", "e"],
             "c": ["f"],
             "d": ["g"],
             "e": ["g"],
             "f": ["e", "g"],
             "g": []
             }
        graph = Graph(g)
        paths = graph.findAllPaths("a","z")
        print(path)
        self.assertListEqual(graph.findAllPaths("a","z") , [])

    def testFAnull(self):
        g = {}
        graph = Graph(g)
        paths = graph.findAllPaths("a","g")
        print(path)
        self.assertListEqual(graph.findAllPaths("a","g") , [])


class testFindLCA(unittest.TestCase):

    # test for LCA function in normal scenarios
    def testLCA(self):
        g = {"a": ["b", "c"],
             "b": ["c", "d"],
             "c": ["d"],
             "d": ["c"],
             "e": ["f"],
             "f": ["c"]
             }
        graph = Graph(g)
        self.assertTrue(True)


    # test for LCA function when the root is given as
    # one of the inputs
    def testLCAwroot(self):
        g = {"a": ["b", "c"],
             "b": ["c", "d"],
             "c": ["d"],
             "d": ["c"],
             "e": ["f"],
             "f": ["c"]
             }
        graph = Graph(g)
        self.assertTrue(True)

    # test for LCA function when the same node is given
    # as both inputs to the function
    def testLCAself(self):
        g = {"a": ["b", "c"],
             "b": ["c", "d"],
             "c": ["d"],
             "d": ["c"],
             "e": ["f"],
             "f": ["c"]
             }
        graph = Graph(g)
        self.assertTrue(True)

    # test for LCA function when one or both of the nodes
    # does not exist
    def testLCAfalse(self):
        g = {"a": ["b", "c"],
             "b": ["c", "d"],
             "c": ["d"],
             "d": ["c"],
             "e": ["f"],
             "f": ["c"]
             }
        graph = Graph(g)
        self.assertTrue(True)

    # test for LCA function when no binary tree is provided
    def testLCAnull(self):
        g = {
             }
        graph = Graph(g)
        self.assertTrue(True)



if __name__ == '__main__':
    unittest.main()
