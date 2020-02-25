#!/bin/python3

import time
import timeit
import sys


class Node:  
    def __init__(self, value): 
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self):  
        self.head = None
        self.tail = None

    def listPrint(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next    

    def appendInt(self):
        appendval = self.head
        while appendval is not None:
            if appendval.value % 2 == 0:
                evenNode = Node(appendval.value)
                if evenList.head is None:
                    evenList.head = evenNode
                else:
                    evenList.tail.next = evenNode
                evenList.tail = evenNode
            else:
                oddNode = Node(appendval.value)
                if oddList.head is None:
                    oddList.head = oddNode
                else:
                    oddList.tail.next = oddNode
                oddList.tail = oddNode
            appendval = appendval.next

t1 = time.clock()
orgList = LinkedList()
orgList.head = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
orgList.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5

evenList = LinkedList()
oddList = LinkedList()

orgList.appendInt()

print('orgList: ')
orgList.listPrint()
print('evenList: ')
evenList.listPrint()
print('oddList: ')
oddList.listPrint()
t2 = time.clock()

# Time complexity:
tcode = """
class Node:  
    def __init__(self, value): 
        self.value = value
        self.next = None

class LinkedList: 
    def __init__(self):  
        self.head = None
        self.tail = None

    def listPrint(self):
        printval = self.head
        while printval is not None:
            print(printval.value)
            printval = printval.next    

    def appendInt(self):
        appendval = self.head
        while appendval is not None:
            if appendval.value % 2 == 0:
                evenNode = Node(appendval.value)
                if evenList.head is None:
                    evenList.head = evenNode
                else:
                    evenList.tail.next = evenNode
                evenList.tail = evenNode
            else:
                oddNode = Node(appendval.value)
                if oddList.head is None:
                    oddList.head = oddNode
                else:
                    oddList.tail.next = oddNode
                oddList.tail = oddNode
            appendval = appendval.next

orgList = LinkedList()
orgList.head = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
orgList.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5

evenList = LinkedList()
oddList = LinkedList()

orgList.appendInt()
"""

time_comp = timeit.repeat(stmt=tcode, repeat=2)
print('min time: ', min(time_comp), 'second')
print('max time: ', max(time_comp), 'second')
print('actual duration: ', t2 - t1, 'sec')

# Space complexity:
print('space usage: ', sys.getsizeof(Node) + sys.getsizeof(LinkedList) + sys.getsizeof(orgList) + sys.getsizeof(evenList) + sys.getsizeof(oddList), 'bytes')
