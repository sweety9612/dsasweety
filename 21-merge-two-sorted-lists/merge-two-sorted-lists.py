# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        prev=ListNode()
        cur1=list1
        cur2=list2
        head=None
        if cur1.val<=cur2.val:
            head=cur1
        else:
            head=cur2
        while cur1!=None and cur2!=None:
            if cur1.val<=cur2.val:
                prev.next=cur1
                prev=cur1
                cur1=cur1.next
            else:
                prev.next=cur2
                prev=cur2
                cur2=cur2.next
            
        
        if cur1:
            prev.next=cur1
        if cur2:
            prev.next=cur2
        return head


        