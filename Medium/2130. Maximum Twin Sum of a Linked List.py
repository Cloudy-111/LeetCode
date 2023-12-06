# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next.next
        stack = []
        stack.append(slow.val)
        while fast and fast.next:
            slow = slow.next
            stack.append(slow.val)
            fast = fast.next.next
        res = 0
        while slow and slow.next:
            slow = slow.next
            res = max(res, slow.val + stack.pop())
        return res
