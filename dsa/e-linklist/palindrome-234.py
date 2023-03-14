'''
Given the head of a singly linked list, return true if it is a
Input: head = [1,2,2,1]
Output: true
'''

from util import ListNode, build

'''
Approach
1. Find Middle Node
2. Reverse the linklist from middle node -> next to last
3 Now comapre from head  and midlle next if all good than valid palindrome 
'''


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


def isPalindrome(head):
    if head.next is None:
        return True

    def middleNode(head):
        slow = head
        fast = head

        while not fast.next is None and not fast.next.next is None:
            fast = fast.next.next
            slow = slow.next
        return slow

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

    middle = middleNode(head)
    reverseLinkList = reverseALinkList(middle.next)
    print(reverseLinkList)

    temp = head
    while reverseLinkList:
        if temp.val != reverseLinkList.val:
            return False
        temp = temp.next
        reverseLinkList = reverseLinkList.next

    return True


for head in [
    # build([1, 2, 2, 1]),
    #
    # build([1, 2, 3, 2, 1]),
    #
    build([1, 2]),
]:
    print(isPalindrome(head))
