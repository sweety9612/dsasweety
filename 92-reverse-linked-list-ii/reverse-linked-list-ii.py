class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move `prev` to the node just before `left`
        for _ in range(left - 1):
            prev = prev.next
        
        # `start` will point to the first node of the sublist to reverse
        # `then` is the node that will be reversed
        start = prev.next
        then = start.next

        # Reverse the sublist using head insertion technique
        for _ in range(right - left):
            start.next = then.next
            then.next = prev.next
            prev.next = then
            then = start.next
        
        return dummy.next
