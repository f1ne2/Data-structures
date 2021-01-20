import unittest
from Tree import Tree


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
        self.assertEqual(new.root.item, 115)

    def test_left_most(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        self.assertEqual(new.left_most(new.root).item, 7)

    def test_compare_to(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        self.assertEqual(new.compare_to(new.root, new.left_most(new.root)), 1)

    def test_clear(self):
        new = Tree()
        new.add(40)
        new.add(34)
        new.add(115)
        new.add(7)
        new.add(60)
        new.clear(new.root)
        self.assertEqual(new.size, 0)


if __name__ == "__main__":
    unittest.main()
