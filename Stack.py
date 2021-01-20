from __future__ import annotations
import sys
from typing import Generic, TypeVar

T = TypeVar("T")


class Stack:
    def __init__(self):
        self.size: int = 0
        self.top = None

    def push(self, item: Generic[T]) -> None:
        new = Node(item)
        if self.size == 0:
            self.top = new
        else:
            new.next = self.top
            self.top = new
        self.size += 1

    def pop(self) -> Generic[T]:
        if self.size == 0:
            print("Stack is empty")
            raise IndexError
        temporary = self.top
        returning = self.top.item
        self.top = self.top.next
        self.size -= 1
        del temporary
        return returning

    def count(self) -> int:
        return self.size

    def peek(self) -> Generic[T]:
        return self.top.item


class Node:
    def __init__(self, item: Generic[T]):
        self.__next = None
        self.__item: Generic[T] = item

    def __eq__(self, other):
        return self.item == other.item

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node: Node) -> None:
        self.__next = node

    @property
    def item(self) -> Generic[T]:
        return self.__item

    @item.setter
    def item(self, temp: Generic[T]) -> None:
        self.__item = temp
