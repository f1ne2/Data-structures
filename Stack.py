import sys
from typing import Any


class Stack:
    def __init__(self):
        self.size: int = 0
        self.top = None

    def push(self, item: int) -> None:
        new = Node(item)
        if self.size == 0:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.size += 1

    def pop(self) -> Any:
        try:
            if self.size == 0:
                raise IndexError
        except:
            print("Stack is empty")
            sys.exit()
        temporary = self.top
        returning = self.top.item
        self.top = self.top.next
        self.size -= 1
        del temporary
        return returning

    def count(self) -> int:
        return self.size

    def peek(self) -> Any:
        return self.top.item


class Node:
    def __init__(self, item: int):
        self.__next = None
        self.__item: Any = item

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node) -> None:
        self.__next = node

    @property
    def item(self) -> Any:
        return self.__item

    @item.setter
    def item(self, temp: Any) -> None:
        self.__item = temp
