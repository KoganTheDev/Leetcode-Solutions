# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        numbers_counter = dict()
        curr_node = head
        prev_node = None
        
        while curr_node != None:
            # number doesn't exist, therefore put it in the dictionary.
            if curr_node.val not in numbers_counter:
                numbers_counter[curr_node.val] = 1
                
                prev_node = curr_node
                curr_node = curr_node.next
            
            # The curr_node is a duplicate of another node.
            elif numbers_counter[curr_node.val] == 1:
                curr_node = curr_node.next
                prev_node.next = curr_node
        
        return head