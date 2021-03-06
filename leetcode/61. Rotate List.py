# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:

# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:

# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
    # Runtime: 48 ms, faster than 57.77% of Python3 online submissions for Rotate List.
    # Memory Usage: 13.1 MB, less than 5.77% of Python3 online submissions for Rotate List.
        p = head
        if p == None:
            return None
        s = []
        l = 0
        while p!=None:
            l+=1
            s.append(p)
            p = p.next
        k = (k-1)%l
        i = l - k -1
        ans = s[i]
        s[-1].next = s[0]
        s[(i-1)%l].next = None
        return ans
    
    
