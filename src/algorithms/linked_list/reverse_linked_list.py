from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    '''
    Example: 1 -> 2 -> 3 -> 4 -> 5
    '''
    if head is None or head.next is None:
        return head
    reversed = reverseList(head.next)
    # When reversed is 5 for example, what is happening here is head is 4
    # we are setting 4.next.next = 4 and then 4.next = None
    # - Which is 5.next = 4
    # - 4.next = None - to set the current node's next pointer to None to avoid cycles
    head.next.next = head
    head.next = None
    return reversed

print(reverseList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
))