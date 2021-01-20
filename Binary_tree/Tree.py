from __future__ import annotations


class Node:
    def __init__(self, item: int):
        self.__left = None
        self.__right = None
        self.__item = item

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, node) -> None:
        self.__right = node

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, node) -> None:
        self.__left = node

    @property
    def item(self) -> int:
        return self.__item

    @item.setter
    def item(self, temp: int) -> None:
        self.__item = temp


class Tree:
    def __init__(self):
        self.size = 0
        self.root = None

    def add(self, item: int):
        if self.size == 0:
            self.root = Node(item)
        else:
            self.add_to(self.root, item)
        self.size += 1

    def add_to(self, node: Node, item: int):
        if item > node.item:
            if not node.right:
                node.right = Node(item)
            else:
                self.add_to(node.right, item)
        elif item < node.item:
            if not node.left:
                node.left = Node(item)
            else:
                self.add_to(node.left, item)
        return

    def tree_contains(self, current: Node):
        if self.size == 0:
            print("Tree is Empty")
            return
        print(current.item, end=" ")
        if current.right:
            self.tree_contains(current.right)
        if current.left:
            self.tree_contains(current.left)
        return

    def remove(self, item: int):
        if self.size == 0:
            print("Tree is Empty")
            return
        self.remove_to(None, self.root, item)
        self.size -= 1

    def remove_to(self, parent: None or Node, current: Node, item: int):
        try:
            if current.item == item:
                self.delete(parent, current)
        except AttributeError:
            print("This element don't exist")
            return
        if current.item < item:
            self.remove_to(current, current.right, item)
        if current.item > item:
            self.remove_to(current, current.left, item)

    def delete(self, parent: Node, current: Node):
        if not parent:
            if not current.right:
                self.root = current.left
            elif not current.left:
                self.root = current.right
            else:
                self.root = current.right
                self.left_most(current.right).left = current.left
        elif self.compare_to(parent, current) > 0:
            if not current.right and not current.left:
                parent.left = None
                del current
            elif current.right and not current.left:
                parent.left = current.right
                del current
            elif current.left and not current.right:
                parent.left = current.left
                del current
            else:
                parent.left = current.right
                self.left_most(current.right).left = current.left
                current.right = None
                del current
        else:
            if not current.right and not current.left:
                parent.right = None
                del current
            elif current.right and not current.left:
                parent.right = current.right
                current.right = None
                del current
            elif current.left and not current.right:
                parent.right = current.left
                current.left = None
                del current
            else:
                parent.right = current.right
                self.left_most(current.right).left = current.left
                current.left = None
                del current

    def left_most(self, current: Node) -> Node:
        for i in range(self.size):
            if current.left:
                current = current.left
            else:
                return current

    def compare_to(self, parent: Node, current: Node) -> int:
        if parent.item > current.item:
            return 1
        elif parent.item < current.item:
            return -1
        elif parent.item == current.item:
            return 0

    def clear(self, current: Node):
        if current.right:
            self.clear(current.right)
        if current.left:
            self.clear(current.left)
        current.right = None
        current.left = None
        del current
        self.size = 0
        return
