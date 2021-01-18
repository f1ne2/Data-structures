import unittest
from Stack import Stack, Node


class TestStack(unittest.TestCase):
    def test_pop(self):
        self.new = Stack()
        self.new.push("2CBA")
        self.assertEqual(self.new.pop(), "2CBA")

    def test_count(self):
        self.new = Stack()
        self.new.push("1CBA")
        self.new.push("2CBA")
        self.assertEqual(self.new.count(), 2)

    def test_peek(self):
        self.new = Stack()
        self.new.push("1CBA")
        self.new.push("2CBA")
        self.assertEqual(self.new.peek(), "2CBA")


class TestNode(unittest.TestCase):
    def SetUp(self):
        self.node_1 = Node("ABC")
        self.node_2 = Node("ABC_2")

    def test_next(self):
        self.new = Stack()
        self.new.push("1CBA")
        self.new.push("2CBA")
        self.assertEqual(self.new.top.next, Node("1CBA"))

    def test_item(self):
        self.new = Stack()
        self.new.push("1CBA")
        self.new.push("2CBA")
        self.assertEqual(self.new.top.item, "2CBA")


if __name__ == "__main__":
    unittest.main()
