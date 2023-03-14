'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

'''
from util import build


def rotateRight(head, k):
    if not head:
        return head
    curr = head
    length = 1

    # calculating length of linkedlist
    while curr.next:
        curr = curr.next
        length += 1

    # now connect end node to head -> treat it as a circle now
    curr.next = head

    # mode of k
    k = length - k % length

    # now shift current until k !=0
    while k > 0:
        curr = curr.next
        k -= 1

    newHead = curr.next
    curr.next = None
    return newHead


for head in [
    build([1, 2, 3, 4, 5]),
    build([]),
    build([1]),
    build([1, 2])
]:
    print(rotateRight(head, 2))

print()
