# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode()
        curr = temp

        while list1 and list2:
            # If list1's value is less than list2's
            if list1.val < list2.val:
                # Set our current node's next pointer to be the list1 value
                curr.next = list1
                # Move the current pointer to the new value
                curr = list1
                # Iterate through the list 
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        curr.next = list1 if list1 else list2

        return temp.next
            
