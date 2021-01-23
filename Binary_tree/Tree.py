from __future__ import annotations


class Node:
    def __init__(self, item: int):
        self.__left = None
        self.__right = None
        self.__item = item
        self.__height = 1

    @property
    def right(self) -> Node:
        return self.__right

    @right.setter
    def right(self, node) -> None:
        self.__right = node

    @property
    def left(self) -> Node:
        return self.__left

    @left.setter
    def left(self, node) -> None:
        self.__left = node

    @property
    def item(self) -> int:
        return self.__item

    @item.setter
    def item(self, current: int) -> None:
        self.__item = current

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, current: int) -> None:
        self.__height = current


class Tree:
    def __init__(self):
        self.size = 0
        self.root = None

    def __eq__(self, other: Node):
        return self.root.item == other.item

    def add(self, item: int) -> None:
        if self.size == 0:
            self.root = Node(item)
        else:
            self.root = self.add_to(self.root, item)
        self.size += 1

    def add_to(self, node: Node, item: int) -> Node:
        if item > node.item and not node.right:
            node.right = Node(item)
        elif item > node.item and node.right:
            node.right = self.add_to(node.right, item)
        elif item < node.item and not node.left:
            node.left = Node(item)
        elif item < node.item and node.left:
            node.left = self.add_to(node.left, item)
        return self.balance(node)

    def tree_contains(self, current: Node, array: list) -> list:
        if self.size == 0:
            return array
        array.append(current)
        if current.right:
            self.tree_contains(current.right, array)
        if current.left:
            self.tree_contains(current.left, array)
        return array

    def remove(self, item: int) -> None:
        if self.size == 0:
            return
        self.remove_to(None, self.root, item)
        self.size -= 1

    def remove_to(self, parent: None or Node, current: Node, item: int) -> None:
        if current.item == item:
            self.delete(parent, current)
            self.root = self.balancing(self.root)
        if current.item < item:
            self.remove_to(current, current.right, item)
        if current.item > item:
            self.remove_to(current, current.left, item)

    def balancing(self, node: Node) -> Node:
        if node.right:
            node.right = self.balancing(node.right)
        if node.left:
            node.left = self.balancing(node.left)
        return self.balance(node)

    def delete(self, parent: Node, current: Node) -> None:
        if not parent:
            if not current.right:
                self.root = current.left
            elif not current.left:
                self.root = current.right
            else:
                self.root = current.right
                self.left_most(current.right).left = current.left
        elif parent.item > current.item:
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

    def clear(self, current: Node) -> None:
        if current.right:
            self.clear(current.right)
        if current.left:
            self.clear(current.left)
        current.right = None
        current.left = None
        del current
        self.size = 0

    def fix_height(self, current: Node) -> None:
        hl = self.height(current.left)
        hr = self.height(current.right)
        if hl > hr:
            current.height = hl+1
        else:
            current.height = hr+1

    def height(self, node: Node or None) -> int:
        if node is None:
            return 0
        else:
            l_height = self.height(node.left)
            r_height = self.height(node.right)
            if l_height > r_height:
                return l_height+1
            else:
                return r_height+1

    def b_factor(self, node: Node):
        return self.height(node.right) - self.height(node.left)

    def rotate_right(self, parent: Node) -> Node:
        current = parent.left
        parent.left = current.right
        current.right = parent
        self.fix_height(parent)
        self.fix_height(current)
        return current

    def rotate_left(self, parent: Node) -> Node:
        current = parent.right
        parent.right = current.left
        current.left = parent
        self.fix_height(parent)
        self.fix_height(current)
        return current

    def balance(self, node: Node) -> Node:
        self.fix_height(node)
        if self.b_factor(node) == 2:
            if self.b_factor(node.right) < 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        if self.b_factor(node) == -2:
            if self.b_factor(node.left) > 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        return node
