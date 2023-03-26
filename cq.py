# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:42:53 2023


@author: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati


Notes:
    
    - No limit to the number of elements in the queue
    
    - The agorithmic complexity is O(n) because there is no loop and the steps are dependent on the number of elements in the list
"""

class Empty(Exception):
  pass


class CircularQueue:
    """Queue implementation using circularly linked list for storage"""""
    
    class _Node:  # Inner class for nodes
        __slots__ = '_element', '_next', '_tail'
        
        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt # points to next node

    def __init__(self):
        self._tail = None # initializes the queue with a single _tail variable
        self._size = 0 # tracking size of queue

    def __len__(self):
        return self._size # returns size of queue

    def is_empty(self):
        return self._size == 0

    def first(self): # returns the head element of queue
        if self.is_empty():
            raise Empty('Circular queue is empty')
        head = self._tail._next
        return head._element


    def dequeue(self): # removes and returns head element
        if self.is_empty():
            raise Empty('Circular queue is empty')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element

    
    def enqueue(self, e): # adds an element to the tail
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
    def rotate(self): # rotates the queue by moving head element to the tail
        if self._size > 0:
            self._tail = self._tail._next
            
    def __str__(self): # create visual representation of the queue
        if self.is_empty():
            return "Empty queue"
        result = []
        current = self._tail._next
        
        while True:
            result.append(str(current._element))
            current = current._next
            if current == self._tail._next:
                break
        return " -> ".join(result) 
        

