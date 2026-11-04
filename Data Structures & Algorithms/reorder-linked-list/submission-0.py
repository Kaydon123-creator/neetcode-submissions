# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # first find the mid 
        fast = slow = head
        prev = ListNode()
        while fast and fast.next :
            prev = slow
            slow = slow.next 
            fast = fast.next.next
        #disconnect two halves

        prev.next = None 

        #slow points to the mid 
        mid = slow

        def reverse(mid):
            prev = None
            dummy = ListNode()
            curr = mid 

            while curr:
                nxt = curr.next
                curr.next = prev 
                prev = curr 
                curr = nxt 

            return prev 

        dummy = ListNode()
        dummy.next = head 

        list1 = reverse(mid)
        list2 = head

        while list1 and list2:
            nxt1, nxt2 = list1.next , list2.next
            list2.next = list1 
            list1.next = nxt2 if nxt2 else nxt1 
            list1 = nxt1 
            list2 = nxt2 

      


        
            

            

        
            


        

        