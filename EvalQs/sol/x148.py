# Generated Fixed Code

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        # Bubble sort implementation
        def bubble_sort(node):
            if not node or not node.next:
                return node
            
            dummy = ListNode(0)
            dummy.next = node
            swapped = True
            while swapped:
                swapped = False
                prev = dummy
                current = dummy.next
                while current.next:
                    if current.val > current.next.val:
                        prev.next = current.next
                        current.next = current.next.next
                        prev.next.next = current
                        prev = prev.next
                        swapped = True
                    else:
                        prev = current
                        current = current.next
            
            return dummy.next
        
        return bubble_sort(head)