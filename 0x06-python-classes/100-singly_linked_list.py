#!/usr/bin/python3
"""Node Class
defines a node of a singly linked list
"""

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")
                                                                                        
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    def __str__(self):
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
            return result
