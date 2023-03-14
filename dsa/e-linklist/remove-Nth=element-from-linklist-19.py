'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
'''

from util import build


def removeNthElementFromLinkList(head, n):
    def reverseALinkList(head):
        prev = None
        curr = head
        while curr:
            future = curr.next
            curr.next = prev
            prev = curr
            curr = future
        head = prev
        return head

    reverseLinkList = reverseALinkList(head)
    temp = reverseLinkList
    print(temp)
    i = 1
    while temp:
        if i == n:
            if temp.next and temp.next.next:
                temp.val = temp.next.val
                temp.next = temp.next.next
                return reverseALinkList(reverseLinkList)
        else:
            i = i + 1
            temp = temp.next

    return reverseALinkList(reverseLinkList)


# for head in [
#     build([1, 2, 3, 4, 5])
# ]:
#     print(removeNthElementFromLinkList(head, 2))

print()


def removeNthFromEnd(head, n):
    slow = fast = head
    for i in range(n):
        fast = fast.next

    if not fast:
        return head.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next

    return head

for head in [
    build([1]),
    build([1, 2, 3, 4, 5,6,7])
]:
    print(removeNthFromEnd(head, 1))

print()
