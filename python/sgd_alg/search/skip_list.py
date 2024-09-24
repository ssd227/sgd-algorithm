'''
skip list 跳跃表


Note
    Generalization of sorted linked lists – so simple to implement

'''

from collections import namedtuple

FWPointer = namedtuple('FWPointer', ['fw', 'span'])


fwp = FWPointer(forward=SkipListNode(), span=2)

# 通过名称访问元素
print(fwp.forward) 
print(fwp.span) 



class SkipListNode:
    def __init__(self, ) -> None:
        self.
        self.bw : SkipListNode
    
    def 

class SkipList:
    def __init__(self) -> None:
        self.header
        self.tail
        self.level
        self.length
    
    def put(self, key, value):
        pass
    
    def get(self, key):
        pass
    
    def size(self):
        pass