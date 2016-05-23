# Regression Testing
# ------------------
# The goal of this problem is for you to write a regression tester
# for the Queue class.
# 
# Begin by finding and fixing all of the bugs in the Queue class. Next,
# define the function regression_test to take in a list of enqueue inputs
# and dequeue indicators (the returned list of the previous problem) and
# repeat those method calls using the fixed Queue.
# 
# That is, after fixing the Queue class, create a new Queue instance,
# and call the method corresponding to the indicator in the list
# for each item in the list:
# 
# Call the enqueue function whenever you come across an integer, using that
#     integer as the argument.
# Call the dequeue function whenever you come across the 'dq' indicator.

import array
import random

# Fix this Queue class
class Queue:
    
    def __init__(self,size_max):
        assert size_max > 0
        self.max = size_max
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array('l', range(size_max))

    def empty(self):
        return self.size == 0

    def full(self):
        return self.size == self.max

    def enqueue(self,x):
        if self.size == self.max:
            return False
        if not type(x) is int:
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
            assert (self
                    .size==0) or (self.size==self.max)


# An example list of enqueue integers and dequeue indicators
inpts = [(574, 0), ('dq', 0), (991, 0), ('dq', 0), ('dq', 1),
         (731, 0), (97, 0), ('dq', 0), (116, 0), ('dq', 0),
         (464, 0), (723, 0), (51, 0), ('dq', 0), (553, 0),
         (390, 0), ('dq', 0), (165, 0), (952, 0), ('dq', 0),
         ('dq', 0), (586, 0), (894, 0), ('dq', 0), ('dq', 0),
         (125, 0), (802, 0), (963, 0), (370, 0), ('dq', 0),
         ('dq', 0), (467, 0), (274, 0), ('dq', 0), (737, 0),
         (665, 0), (996, 0), (604, 0), (354, 0), ('dq', 0),
         (415, 0), ('dq', 0), ('dq', 0), ('dq', 0), ('dq', 0),
         ('dq', 0), (588, 0), (702, 0), ('dq', 0), ('dq', 0),
         (887, 0), ('dq', 0), (286, 0), (493, 0), (105, 0),
         ('dq', 0), (942, 0), ('dq', 0), (167, 0), (88, 0),
         ('dq', 0), (145, 0), ('dq', 0), (776, 0), ('dq', 0),
         ('dq', 0), ('dq', 0), ('dq', 0), (67, 0), ('dq', 0),
         ('dq', 0), (367, 0), ('dq', 0), (429, 0), (996, 0),
         (508, 0), ('dq', 0), ('dq', 0), (295, 0), ('dq', 0),
         ('dq', 0), ('dq', 0), (997, 0), ('dq', 0), (29, 0),
         (669, 0), ('dq', 0), (911, 0), ('dq', 0), ('dq', 0),
         (690, 0), (169, 0), (730, 0), (172, 0), (161, 0),
         (966, 0), ('dq', 0), (865, 0), ('dq', 0), (348, 0)]
inpts = [('dq', 1), ('dq', 1), ('a', 0), ('dq', 1), (-3928418816584465857, 0), ('dq', 1), (593355370187753285, 0), ('dq', 1), (3440478558002288321, 0), ('dq', 1), ('dq', 1), (1445443977180690564, 0), (-404138916641062521, 0), ('dq', 1), ('dq', 1), ('dq', 1), ('dq', 1), ('dq', 1), ('dq', 1), ('dq', 1), (2996308530682823061, 0), ('dq', 1), (-8832354834852981569, 0), ('dq', 1), (2202325682203359923, 0), (3970738276718207157, 0), (6790551829613502772, 0), ('dq', 1), ('dq', 1), ('dq', 1), (7041739735502843433, 0), ('dq', 1), ('dq', 1), ('dq', 1), (6230897435446255948, 0), (3363780247525337843, 0), (532141626829625281, 0), (8163376851584016906, 0), (-5541893706980206618, 0), (-6268677466301874204, 0), (765831116398069968, 0), ('dq', 1), (-2311410521620388339, 0), (-1880880153860498293, 0), (-4704437137564894473, 0), (-8487742386355728909, 0), (-530388188445978864, 0), ('dq', 0), (-2685740021479561991, 0), (5686876369523836482, 0), (-380855647095623301, 0), ('dq', 0), (-6360610263457090046, 0), (6503574941584409322, 0), (-7513889967281595280, 0), (1082405069974034950, 0), (3732252409979775198, 0), (-8687068243842657866, 0), (-9143659371712577248, 0), ('dq', 0), (-3350027632437928261, 0), ('dq', 0), (6796512559265927070, 0), ('dq', 0), (6082248631315809164, 0), ('dq', 0), (-441619445617289930, 0), ('dq', 0), ('dq', 0), ('dq', 0), (-6341902575117821164, 0), ('dq', 0), (-2547856939930800230, 0), ('dq', 0), ('dq', 0), ('dq', 0), (-4019050615813331323, 0), ('dq', 0), ('dq', 0), ('dq', 0), (-3832315141815893533, 0), (4300669947949887779, 0), (1273946064658791852, 0), (-4845363560792820027, 0), ('dq', 0), (-7160395978336947016, 0), ('dq', 0), ('dq', 0), (-7807841171369491503, 0), ('dq', 0), ('dq', 0), (-8963834630915664051, 0), (3793487587831082016, 0), ('dq', 0), (-7883699344810026125, 0), ('dq', 0), ('dq', 0), ('dq', 0), ('dq', 0), (3458607869082384598, 0)]

def checkInput(ipt):
    if not type(ipt) is list:
        return False
    for i in ipt:
        if (not type(i) is tuple) and len(i) == 2:
            return False
        if type(i[0]) is str and i[0] != 'dq':
            return False
        if not ((type(i[0]) is int or type(i[0]) is str) and type(i[1]) is int):
            return False
    return True

# Write a regression tester for the Queue class
def regression_test(inpts):
    l = 10
    q = Queue(l)
    if(not checkInput(inpts)):
        return
    if(len(inpts) <= 0):
        return
    
    for t in inpts:
        if type(t[0]) is str and t[0] == 'dq':
            q.dequeue()
        else:
            x = t[0]
            if not type(x) is int:
                continue
            q.enqueue(t[0])
        q.checkRep()
            
regression_test(inpts)
