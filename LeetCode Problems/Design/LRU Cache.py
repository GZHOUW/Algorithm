'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
The cache is initialized with a positive capacity.

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail  # connect head and tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)  # move the node to end of linked list
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:  # already exist ---> update value (remove then add)
            self._remove(self.cache[key])
        n = Node(key, value) # create new node to add
        self._add(n)  # add to linked list
        self.cache[key] = n  # add to cache
        if len(self.cache) > self.capacity:
            n = self.head.next # the first node of linked list is the least recently used, remove it
            self._remove(n)  # remove from linked list
            del self.cache[n.key]  # remove from cache

    def _remove(self, node):  # remove the node from linked list
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node): # addLast
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
