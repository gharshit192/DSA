'''
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

'''
from util import build



def main(head):
    slow = head
    fast = head
    if head.next is None:
        return head
    elif head.next.next is None:
        return head.next
    else:
        while not fast is None and not fast.next is None:
            fast = fast.next.next
            slow = slow.next
        return slow


for head in [
    build([1, 2, 3, 4]),
    build([1]),
    build([1, 2, 3, 4, 5]),
]:
    print(main(head))

print()
