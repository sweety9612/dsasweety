# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head:
            return
        if not head.next:
            return head
        prev=None
        curr=head
        nextnode=curr.next

        while nextnode:
            curr.next=prev
            prev=curr
            curr=nextnode
            nextnode=nextnode.next
        curr.next=prev    
        head=curr
        return head

        

        
        