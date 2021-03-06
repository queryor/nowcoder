# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.

# Example:

# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ## 两个指针 分别往后移动
        if head==None or head.next == None:
            return head
        res = ListNode(-1)
        res.next = head
        pre = res
        cur = pre
        while cur.next!=None:
            if cur.next.val < x:
                if cur == pre:
                    pre = pre.next
                    cur = cur.next
                else: 
                    t = pre.next
                    pre.next = cur.next
                    cur.next = cur.next.next
                    pre = pre.next
                    pre.next = t
            else: 
                cur= cur.next
        return res.next            