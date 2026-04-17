# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l_res = ListNode()
        l_pointer = l_res
        carry = 0
        
        while l1 and l2:
            # 計算這個位數相加跟需要進位多少
            a, b = l1.val, l2.val
            inc = (a + b + l_pointer.val) % 10
            carry = (a + b) // 10

            #更新目前位數
            l_pointer.val = inc
            
            # 只要l1,l2有一個有下一位或是有carry我就可以放心產生下一位
            if carry or l1.next or l2.next:
                l_pointer.next = ListNode(carry)
                l_pointer = l_pointer.next

            # 更新l1,l2
            l1, l2 = l1.next, l2.next
                

        # 只剩l1
        while l1:
            inc = (l1.val + l_pointer.val) % 10
            carry = (l1.val + l_pointer.val) // 10
            
            l_pointer.val = inc
            if carry:
                l_pointer.next = ListNode(carry)
                l_pointer = l_pointer.next
            
            l1 = l1.next

            
        # 只剩l2
        while l2:
            inc = (l2.val + l_pointer.val) % 10
            carry = (l2.val + l_pointer.val) // 10
            
            l_pointer.val = inc
            if carry:
                l_pointer.next = ListNode(carry)
                l_pointer = l_pointer.next

            l2 = l2.next
        
        return l_res




            