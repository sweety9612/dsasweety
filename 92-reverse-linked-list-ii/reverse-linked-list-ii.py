# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head:
            return
        if not head.next:
            return head
        if left == right:
            return head
        leftnode=ListNode(0,None)
        prev=None
        cur=head
        nextnode=head.next 
        revhead=ListNode(0,None)
        flag=0
        count=0
        while(nextnode):
            count+=1

            if count == left:
                revhead=cur
                flag=1
            if flag:
                cur.next=prev
                prev=cur

            if count == right:
                
                leftnode.next=cur
                revhead.next=nextnode
                if left == 1:
                    head=cur
                return head

            if not flag:
                leftnode=cur
            cur=nextnode
            nextnode=nextnode.next
        cur.next=prev
        if left==1:
            head=cur
        else:
            leftnode.next=cur
            revhead.next=nextnode

        print(head)
        
        return head
            

                

        