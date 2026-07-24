# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        curNode = ListNode()
        dummy = curNode
        while list1 and list2:
            nextNode = list1 if list1.val < list2.val else list2
            if list1.val < list2.val:
                list1 = list1.next
            else:
                list2 = list2.next
            
            curNode.next = nextNode
            curNode = curNode.next

        
        if list1:
            curNode.next = list1
        if list2:
            curNode.next = list2
        

        return dummy.next


                

