# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head.next
        p2 = head
        p2.next = None


        while(p1):
            tmp = p1
            p1 = p1.next
            tmp.next = p2
            p2 = tmp
        return p2