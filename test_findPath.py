import unittest
import collections
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
        #print(path)
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
        #print(path)
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
        #print(path)
        self.assertListEqual(graph.find_path("a", "g"), [])

    # test for findPath function when no binary tree
    # is provided
    def testFPnull(self):
        g = {
             }
        graph = Graph(g)
        path = graph.find_path("a", "d")
        #print(path)
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
        print(paths)
        self.assertListEqual(sorted(graph.findAllPaths("a","g")) , sorted([['a', 'b', 'd', 'g'], ['a', 'b', 'e', 'g'], ['a', 'c', 'f', 'g'], ['a', 'c', 'f', 'e', 'g']]))

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
        print(paths)
        self.assertListEqual(sorted(graph.findAllPaths("c","c")) , sorted([['c']]))

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
        print(paths)
        self.assertListEqual(sorted(graph.findAllPaths("d","g")) , sorted([['d', 'g']]))
        paths = graph.findAllPaths("f", "g")
        print(paths)
        self.assertListEqual(sorted(graph.findAllPaths("f", "g")), sorted([['f', 'g'], ['f', 'e', 'g']]))

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
        print(paths)
        self.assertListEqual(graph.findAllPaths("a","z") , [])

    def testFAnull(self):
        g = {}
        graph = Graph(g)
        paths = graph.findAllPaths("a","g")
        print(paths)
        self.assertListEqual(graph.findAllPaths("a","g") , [])


class testFindLCA(unittest.TestCase):

    # test for LCA function in normal scenarios
    def testLCA(self):
        g = {"a": ["b", "c"],
             "b": ["d", "e"],
             "c": ["f"],
             "d": ["g"],
             "e": ["g"],
             "f": ["e", "g"],
             "g": []
             }
        graph = Graph(g)
        self.assertEqual(graph.findLCA("a", "d", "e"), "b")
        self.assertEqual(graph.findLCA("a", "d", "f"), "a")


    # test for LCA function when the root is given as
    # one of the inputs
    def testLCAwroot(self):
        g = {"a": ["b", "c"],
             "b": ["d", "e"],
             "c": ["f"],
             "d": ["g"],
             "e": ["g"],
             "f": ["e", "g"],
             "g": []
             }
        graph = Graph(g)
        self.assertEqual(graph.findLCA("a", "a", "e"), "a")

    # test for LCA function when the same node is given
    # as both inputs to the function
    def testLCAself(self):
        g = {"a": ["b", "c"],
             "b": ["d", "e"],
             "c": ["f"],
             "d": ["g"],
             "e": ["g"],
             "f": ["e", "g"],
             "g": []
             }
        graph = Graph(g)
        self.assertEqual(graph.findLCA("a", "d", "d"), "d")

    # test for LCA function when one or both of the nodes
    # does not exist
    def testLCAfalse(self):
        g = {"a": ["b", "c"],
             "b": ["d", "e"],
             "c": ["f"],
             "d": ["g"],
             "e": ["g"],
             "f": ["e", "g"],
             "g": []
             }
        graph = Graph(g)
        self.assertEqual(graph.findLCA("a", "d", "i"), -1)

    # test for LCA function when no binary tree is provided
    def testLCAnull(self):
        g = {
             }
        graph = Graph(g)
        self.assertEqual(graph.findLCA("a", "d", "i"), -1)



if __name__ == '__main__':
    unittest.main()
