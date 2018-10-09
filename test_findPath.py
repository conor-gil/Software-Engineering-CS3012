import unittest
from LCA import Node
from LCA import findPath
from LCA import findLCA


class testFindPath(unittest.TestCase):

    # test for findPath function in normal scenarios
    def testFindPath(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        path = []
        self.assertTrue(findPath(root, path, 6))
        self.assertListEqual(path, [1, 3, 6])

        path = []
        self.assertTrue(findPath(root, path, 4))
        self.assertListEqual(path, [1, 2, 4])

    # test for findPath function from the root to itself
    def testFProot(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        path = []
        self.assertTrue(findPath(root, path, 1))
        self.assertListEqual(path, [1])

    # test for findPath function when the given node
    # doesn't exist
    def testFPfalse(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        path = []
        self.assertFalse(findPath(root, path, 8))
        self.assertListEqual(path, [])

    # test for findPath function when no binary tree
    # is provided
    def testFPnull(self):
        root = None
        path = []
        self.assertFalse(findPath(root, path, 8))
        self.assertListEqual(path, [])

    #need to change find path tests to test directed acylcic graph

class testFindLCA(unittest.TestCase):

    # test for LCA function in normal scenarios
    def testLCA(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root,4,5), 2)
        self.assertEqual(findLCA(root,4,6), 1)

    # test for LCA function when the root is given as
    # one of the inputs
    def testLCAwroot(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root, 1, 6), 1)
        self.assertEqual(findLCA(root, 1, 5), 1)

    # test for LCA function when the same node is given
    # as both inputs to the function
    def testLCAself(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root, 7, 7), 7)
        self.assertEqual(findLCA(root, 1, 1), 1)

    # test for LCA function when one or both of the nodes
    # does not exist
    def testLCAfalse(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        self.assertEqual(findLCA(root,4,8), -1)
        self.assertEqual(findLCA(root, 10, 8), -1)

    # test for LCA function when no binary tree is provided
    def testLCAnull(self):
        root = None
        self.assertEqual(findLCA(root,4,8), -1)
        self.assertEqual(findLCA(root, 10, 8), -1)



if __name__ == '__main__':
    unittest.main()
