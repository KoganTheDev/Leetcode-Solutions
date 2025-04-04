# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # Edge case:
        if headA == None or headB == None:
            return None
        
        listA_set = set()
        
        current = headA
        # Insert the values into the set
        while current:
            listA_set.add(current)
            current = current.next
            
        # Now check if there's a node that acts as an intersection between the two lists
        current = headB
        while current:
            if current in listA_set:
                return current
            current = current.next

        # In a case in which no node was found
        return None