# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## [Solution 1](#solution-1-code)


<a id="solution-1-code"></a>
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur.next
        
        n = length - n

        if n == 0:
            return head.next

        cur = head
        dummy = cur
        cnt = 0

        while cur:
            cnt += 1
            if cnt == n:
                nxt = cur.next.next
                cur.next = nxt
            
            cur = cur.next

        return dummy
```
