# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        if not head:
            return
        if not head.next:
            return head
        
        slow=head
        fast=slow
        

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        return slow
        