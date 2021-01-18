import unittest
from Stack import Stack, Node


class TestStack(unittest.TestCase):
    def SetUp(self):
        self.size = 0
        self.new = Stack()
        self.new.push("2CBA")

    def test_pop(self):
        self.assertEqual(self.new.pop, "CBA")

    def test_count(self):
        self.new.push("2CBA")
        self.assertEqual(self.new.count, 1)

    def test_peek(self):
        self.assertEqual(self.new.peek, "2CBA")


if __name__ == "__main__":
    unittest.main()