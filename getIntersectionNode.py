# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Time Complexity: O(m + n), where m is the length of list A 
                      and n is the length of list B
    Space Complexity: O(1)
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # If either of the lists is empty, there is no intersection.
        if headA is None or headB is None:
            return None
        
        # Calculate the length of list A.
        lenA = 0
        curr = headA
        while curr is not None:
            lenA += 1
            curr = curr.next
        
        # Calculate the length of list B.
        lenB = 0
        curr = headB
        while curr is not None:
            lenB += 1
            curr = curr.next
        
        # Align the heads of both lists.
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
        
        # Traverse both lists simultaneously to find the intersection node.
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        # Return the intersection node.
        return headA
