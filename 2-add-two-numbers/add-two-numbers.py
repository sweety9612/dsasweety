# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        dummy_head = ListNode(0)

        temp=dummy_head
        while l1 or l2 or  carry:
            val1=0
            val2=0
            if l1:
                val1=l1.val if l1.val else 0
            if l2:
                val2=l2.val if l2.val else 0
            sumval=val1+val2+carry
            carry = sumval // 10
            nodeval = sumval % 10
            newNode=ListNode(nodeval)
            temp.next=newNode
            temp=temp.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dummy_head.next
            

            

        