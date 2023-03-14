'''
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


Example 1:


Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list. The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node.
Example 2:


Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.
Example 3:


Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.


Constraints:

The number of nodes in the list is in the range [1, 105].
1 <= Node.val <= 105
Accepted
175.8K
Submissions
294.8K
Acceptance Rate
59.6%
Seen this question in a real interview before?
1/4
Yes
No
Discussion (18)
Similar Questions
Related Topics
Copyright ©️ 2023 LeetCode All rights reserved

'''
from util import build


def deleteMiddle(head):
    if head.next is None:
        return None
    slow = fast = head
    while not fast is None and not fast.next is None:
        fast = fast.next.next
        slow = slow.next
    if not slow is None and not slow.next is None:
        slow.val = slow.next.val
        slow.next = slow.next.next
    else:
        head.next = None

    return head


for head in [
    # build([1, 2, 3, 4]),
    #
    # build([1, 2, 3, 4,5]),
    #
    build([1])
]:
    print(deleteMiddle(head))
