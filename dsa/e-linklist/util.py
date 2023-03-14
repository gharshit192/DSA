from dataclasses import dataclass


@dataclass
class ListNode:
    val: int = 0
    next: 'ListNode' = None

    def __str__(self):
        temp, nums = self, []
        while temp:
            nums.append(temp.val)
            temp = temp.next
        return str(nums)


def add(head, val):
    if not head:
        return ListNode(val)
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = ListNode(val)
    return head


def build(nums):
    head = None
    for val in nums:
        head = add(head, val)
    return head if head else []


def middleNode(head):
    slow = head
    fast = head
    if head.next is None:
        return head
    elif head.next.next is None:
        return head.next
    else:
        while not fast.next is None and not fast.next.next is None:
            fast = fast.next.next
            slow = slow.next
        return slow
