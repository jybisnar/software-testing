# TASK:
#
# Write a random tester for the Queue class.
# The random tester should repeatedly call 
# the Queue methods on random input in a 
# semi-random fashion. for instance, if 
# you wanted to randomly decide between 
# calling enqueue and dequeue, you would 
# write something like this:
#
# q = Queue(500)
# if (random.random() < 0.5):
#     q.enqueue(some_random_input)
# else:
#     q.dequeue()
#
# You should call the enqueue, dequeue, 
# and checkRep methods several thousand 
# times each.

import array
import random
from collections import deque

class Queue:
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('i', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        self.data[self.tail] = x
        self.size += 1
        self.tail += 1
        if self.tail == self.max:
            self.tail = 0
        return True

    def dequeue(self):
        if self.size == 0:
            return None
        x = self.data[self.head]
        self.size -= 1
        self.head += 1
        if self.head == self.max:
            self.head = 0
        return x

    def checkRep(self):
        assert self.tail >= 0
        assert self.tail < self.max
        assert self.head >= 0
        assert self.head < self.max
        if self.tail > self.head:
            assert (self.tail-self.head) == self.size
        if self.tail < self.head:
            assert (self.head-self.tail) == (self.max-self.size)
        if self.head == self.tail:
            assert (self.size==0) or (self.size==self.max)


# Write a random tester for the Queue class.
def test():
    for j in range(10):
        sz = random.randint(1, 10000)
        q = Queue(sz)
        a = list()
        r = random.randint(999, 10000)
        t_size = 0
        for i in range(r):
            if random.random() < 0.5:
                s = random.randint(1,100000000)
                if t_size == sz:
                    assert q.full()
                    assert not q.enqueue(s)
                else:
                    assert q.enqueue(s)
                    a.append(s)
                    t_size+=1
            else:
                if t_size == 0:
                    assert q.empty()
                    assert q.dequeue() == None
                else:
                    out = q.dequeue()
                    val = a.pop(0)
                    assert out == val
                    t_size-=1
            q.checkRep()
test()


