
from collections import deque

class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.cache_history = deque()

    def get(self, key):
        if key in self.cache.keys():
            if self.is_last_key(key):
                return self.cache[key]
            
            if self.cache_history[0] == key:    
                aux = self.cache_history.popleft()
                self.cache_history.append(aux)
                return self.cache[key]

            self.cache_history.remove(key)
            self.cache_history.append(key)
            return self.cache[key]
        return -1

    def set(self, key, value):

        if self.capacity <= 0:
            return None

        if key in self.cache.keys():
            if not self.is_last_key(key):
                self.cache_history.remove(key)
                self.cache_history.append(key)
        else:
            self.cache_history.append(key)

            if len(self.cache) == self.capacity:
                aux = self.cache_history.popleft()
                del self.cache[aux]
        
        self.cache[key] = value

    def is_last_key(self, key):
        return self.cache_history[-1] == key
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

assert our_cache.get(1) == 1
assert our_cache.get(2) == 2
assert our_cache.get(9) == -1

our_cache.set(5, 5) 
our_cache.set(6, 6)
assert our_cache.get(3) == -1

our_cache = LRU_Cache(2)
assert our_cache.get(2) == -1
assert our_cache.set(2, 6) == None 
assert our_cache.get(1) == -1
assert our_cache.set(1, 5) == None
assert our_cache.set(1, 2) ==  None
assert our_cache.get(1) == 2
assert our_cache.get(2) == 6

our_cache = LRU_Cache(2)
assert our_cache.set(2, 1) == None
assert our_cache.set(3, 2) == None
assert our_cache.get(3) == 2
assert our_cache.get(2) == 1
assert our_cache.set(4, 3) == None
assert our_cache.get(2) == 1

our_cache = LRU_Cache(3)
assert our_cache.set(1, 1) == None
assert our_cache.set(2, 2) == None
assert our_cache.set(3, 3) == None
assert our_cache.set(4, 4) == None
assert our_cache.get(4) == 4
assert our_cache.get(3) == 3
assert our_cache.get(2) == 2
assert our_cache.get(1) == -1
assert our_cache.set(5, 5) == None
assert our_cache.get(1) == -1
assert our_cache.get(2) == 2
assert our_cache.get(3) == 3
assert our_cache.get(4) == -1
assert our_cache.get(5) == 5


our_cache = LRU_Cache(10)
assert our_cache.set(10, 13) == None
assert our_cache.set(3, 17) == None
assert our_cache.set(6, 11) == None
assert our_cache.set(10, 5) == None
assert our_cache.set(9, 10) == None
assert our_cache.get(13) == -1
assert our_cache.set(2, 19) == None
assert our_cache.get(2) == 19
assert our_cache.get(3) == 17
assert our_cache.set(5, 25) == None
assert our_cache.get(8) == -1
assert our_cache.set(9, 22) == None
assert our_cache.set(5, 5) == None
assert our_cache.set(1, 30) == None
assert our_cache.get(11) == -1
assert our_cache.set(9, 12) == None
assert our_cache.get(7) == -1
assert our_cache.get(5) == 5
assert our_cache.get(8) == -1
assert our_cache.get(9) == 12
assert our_cache.set(4, 30) == None
assert our_cache.set(9, 3) == None
assert our_cache.get(9) == 3
assert our_cache.get(10) == 5
assert our_cache.get(10) == 5
assert our_cache.set(6, 14) == None
assert our_cache.set(3, 1) == None
assert our_cache.get(3) == 1
assert our_cache.set(10, 11) == None
assert our_cache.get(8) == -1
assert our_cache.set(2, 14) == None
assert our_cache.get(1) == 30
assert our_cache.get(5) == 5
assert our_cache.get(4) == 30
assert our_cache.set(11, 4) == None
assert our_cache.set(12, 24) == None
assert our_cache.set(5, 18) == None
assert our_cache.get(13) == -1
assert our_cache.set(7, 23) == None
assert our_cache.get(8) == -1
assert our_cache.get(12) == 24
assert our_cache.set(3, 27) == None
assert our_cache.set(2, 12) == None
assert our_cache.get(5) == 18
assert our_cache.set(2, 9) == None
assert our_cache.set(13, 4) == None
assert our_cache.set(8, 18) == None
assert our_cache.set(1, 7) == None
assert our_cache.get(6) == -1
assert our_cache.set(9, 29) == None
assert our_cache.set(8, 21) == None
assert our_cache.get(5) == 18
assert our_cache.set(6, 30) == None
assert our_cache.set(1, 12) == None
assert our_cache.get(10) == -1
assert our_cache.set(4, 15) == None
assert our_cache.set(7, 22) == None
assert our_cache.set(11, 26) == None
assert our_cache.set(8, 17) == None
assert our_cache.set(9, 29) == None
assert our_cache.get(5) == 18
assert our_cache.set(3, 4) == None
assert our_cache.set(11, 30) == None
assert our_cache.get(12) == -1
assert our_cache.set(4, 29) == None
assert our_cache.get(3) == 4
assert our_cache.get(9) == 29
assert our_cache.get(6) == 30
assert our_cache.set(3, 4) == None
assert our_cache.get(1) == 12
assert our_cache.get(10) == -1
assert our_cache.set(3, 29) == None
assert our_cache.set(10, 28) == None
assert our_cache.set(1, 20) == None
assert our_cache.set(11, 13) == None
assert our_cache.get(3) == 29
assert our_cache.set(3, 12) == None
assert our_cache.set(3, 8) == None
assert our_cache.set(10, 9) == None
assert our_cache.set(3, 26) == None
assert our_cache.get(8) == 17
assert our_cache.get(7) == 22
assert our_cache.get(5) == 18
assert our_cache.set(13, 17) == None
assert our_cache.set(2, 27) == None
assert our_cache.set(11, 15) == None
assert our_cache.get(12) == -1
assert our_cache.set(9, 19) == None
assert our_cache.set(2, 15) == None
assert our_cache.set(3, 16) == None
assert our_cache.get(1) == 20
assert our_cache.set(12, 17) == None
assert our_cache.set(9, 1) == None
assert our_cache.set(6, 19) == None
assert our_cache.get(4) == -1
assert our_cache.get(5) == 18
assert our_cache.get(5) == 18
assert our_cache.set(8, 1) == None
assert our_cache.set(11, 7) == None
assert our_cache.set(5, 2) == None
assert our_cache.set(9, 28) == None
assert our_cache.get(1) == 20
assert our_cache.set(2, 2) == None
assert our_cache.set(7, 4) == None
assert our_cache.set(4, 22) == None
assert our_cache.set(7, 24) == None
assert our_cache.set(9, 26) == None
assert our_cache.set(13, 28) == None
assert our_cache.set(11, 26) == None