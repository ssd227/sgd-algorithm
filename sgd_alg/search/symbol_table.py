"""
Symbol Table interface

Values are not null.
Method get() returns null if key not present.
Method put() overwrites old value with new value.

Symbol table
    朴素的实现，直接unorder array 线性查找、插入、删除
    二分查找实现（双order array实现）， 插入删除仍为线性，search（检索） logN

"""


class STInterface:
    def __init__(self):
        pass

    def put(self, key, value):
        raise NotImplementedError("Should have implemented this")

    def get(self, key):
        raise NotImplementedError("Should have implemented this")

    def delete(self, key):
        raise NotImplementedError("Should have implemented this")

    def contains(self, key) -> bool:
        raise NotImplementedError("Should have implemented this")

    def is_empty(self) -> bool:
        raise NotImplementedError("Should have implemented this")

    def size(self) -> int:
        raise NotImplementedError("Should have implemented this")
