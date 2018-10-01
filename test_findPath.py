import unittest
from LCA import Node
from LCA import findPathgit 


class testFindPath(unittest.TestCase):

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

    def testFPnull(self):
        root = None
        path = []
        self.assertFalse(findPath(root, path, 8))
        self.assertListEqual(path, [])



if __name__ == '__main__':
    unittest.main()
