#!/usr/bin/python3
"""
a class Node that defines a node of a singly linked list by
"""
class Node:
    """
    Private instance attribute: data:
property def data(self): to retrieve it
property setter def data(self, value):
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        getter
        Return: data
        """
        return self.__data
    @data.setter
    def data(self, value):
        """
        setter
        attributes:
        value: set data to value if int
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    @property
    def next_node(self):
        """
        getter
        Return: next_node
        """
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        """
        setter
        attributes:
        value: sets next_node, 
        """
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """
    Private instance attribute: data:
property def data(self): to retrieve it
property setter def data(self, value):
    """
    def __init__(self):
        self.head = None

    def __str__(self):
        """
        string representation of singlylinkedlist
        """
        string = ""
        temp = self.__head
        while temp is not None:
            string += str(temp.data)
            temp = temp.next_node
            if temp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        insert new nodes into list
        """
        new = Node(value)

        if self.__head is None:
            self.__head = new
            return

        temp = self.__head
        if new.data < temp.data:
            new.next_node = self.__head
            self.__head = new
            return
        while (temp.next_node is not None) and (new.data > temp.next_node.data):
            temp = temp.next_node
        new.next_node = temp.next_node
        temp.next_node = new
        return
