import unittest
from Tree import Tree, Node


class TestNode(unittest.TestCase):
    def test_right(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        self.assertEqual(new.root.right.item, 115)

    def test_left(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        self.assertEqual(new.root.left.left.item, 7)

    def test_item(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        self.assertEqual(new.root.right.left.item, 60)


class TestTree(unittest.TestCase):
    def test_add(self):
        new = Tree()
        new.add(400)
        self.assertEqual(new.size, 1)
        self.assertEqual(new.root.item, 400)

    def test_remove(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        new.remove(40)
        self.assertEqual(new.root.item, 34)

    def test_left_most(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        self.assertEqual(new.left_most(new.root).item, 7)

    def test_clear(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        new.clear(new.root)
        self.assertEqual(new.size, 0)

    def test_tree_contains(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        check_arr = [40, 115, 60, 34, 7]
        arr = []
        arr = new.tree_contains(new.root, arr)
        for i in range(len(arr)):
            self.assertEqual(arr[i].item, check_arr[i])

    def test_balancing(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        self.assertEqual(new.balancing(new.root.left.left).item, 7)

    def test_height(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        self.assertEqual(new.height(new.root), 3)

    def test_b_factor(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(50)
        self.assertEqual(new.b_factor(new.root), 0)

    def test_fix_height(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(50)
        new.fix_height(new.root)
        self.assertEqual(new.root.height, 3)

    def test_rotate_left(self):
        new = Tree()
        res = Tree()
        new.root = Node(40)
        new.root.right = Node(115)
        new.root.right.right = Node(135)
        res.root = Node(115)
        res.root.right = Node(135)
        res.root.left = Node(40)
        self.assertEqual(new.rotate_left(new.root), res)

    def test_rotate_right(self):
        new = Tree()
        res = Tree()
        new.root = Node(40)
        new.root.left = Node(34)
        new.root.left.left = Node(14)
        res.root = Node(34)
        res.root.right = Node(40)
        res.root.left = Node(14)
        self.assertEqual(new.rotate_right(new.root), res)

    def test_balance(self):
        new = Tree()
        res = Tree()
        new.root = Node(40)
        new.root.right = Node(44)
        new.root.left = Node(14)
        new.root.right.right = Node(54)
        new.root.right.left = Node(43)
        new.root.right.right.right = Node(55)
        res.root = Node(44)
        res.root.right = Node(54)
        res.root.left = Node(40)
        res.root.left.left = Node(14)
        res.root.right.right = Node(55)
        res.root.left.right = Node(43)
        self.assertEqual(new.balance(new.root), res)


if __name__ == "__main__":
    unittest.main()
