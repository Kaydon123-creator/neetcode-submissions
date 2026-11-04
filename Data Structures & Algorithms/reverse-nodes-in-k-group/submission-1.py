# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, node):
            curr = node 
            prev = None 

            while curr :
                nxt = curr.next
                curr.next = prev 
                prev = curr 
                curr = nxt 
            return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  
        if not head :
            return head
        count = 1 
        start = head
        while head and head.next and count < k:
            head = head.next 
            count+=1 

        if count < k:
            return start 

        nxt = head.next
        head.next = None 
        prev_start = start
        start = self.reverse(start)
        prev_start.next = self.reverseKGroup(nxt, k) 

        return start


        

        
        


        