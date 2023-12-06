# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        cnt = 0
        while tmp:
            cnt += 1
            tmp = tmp.next
        tmp = head
        pt = cnt // 2
        if pt == 0:
            return None
        i = 1
        while tmp:
            if i != pt:
                tmp = tmp.next
            else:
                tmp.next = tmp.next.next
            i += 1
        return head
