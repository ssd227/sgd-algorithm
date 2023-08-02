# public ListNode reverseList(ListNode head) {
#     if (head == null || head.next == null) return head;
#     ListNode p = reverseList(head.next);
#     head.next.next = head;
#     head.next = null;
#     return p;
# }

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
        if not head:
            return None

        if head and head.next is None:
            return head
        
        p = self.reverseList(head.next)

        head.next.next = head
        head.next = None
        return p