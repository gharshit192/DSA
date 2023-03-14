from util import build


def main(head, pos):
    if pos < 0 :
        return False
    len = 1
    while head:
        if pos <= len:
            return True
        head = head.next
        len += 1
    return False


for head in [
    build([1, 2, 3, 4, 5]),
    build([]),
    build([1]),
    build([1, 2])
]:
    print(main(head, 2))
