class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # Put the content of the linked list in an array.
        content = []
        
        while head:
            content.append(head.val)
            head = head.next
        
        # Compare the list with its reverse
        return content == content[::-1]