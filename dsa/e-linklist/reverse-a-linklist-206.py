from util import build, ListNode


# T=n,S=n

def main1(head):
    nums = []
    temp = head
    while temp:
        nums.append(temp.val)
        temp = temp.next
    dummy = tail = ListNode(-1)
    for i in range(len(nums) - 1, -1, -1):
        tail.next = ListNode(nums[i])
        tail = tail.next

    return dummy.next


# # T=n,S=1

def main(head):
    prev = None
    curr = head
    while curr:
        future = curr.next
        curr.next = prev
        prev = curr
        curr = future
    head = prev
    return head


for head in [
    build([1]),
    build([1, 2, 3, 4, 5]),
    build([1, 2])
]:
    print(main(head))

print()
