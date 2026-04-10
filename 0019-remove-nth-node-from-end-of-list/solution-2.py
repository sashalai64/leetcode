class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        
        if length == n:
            return head.next

        step = length - n - 1
        cur = head
        
        for _ in range(step):
            cur = cur.next
        
        cur.next = cur.next.next

        return head