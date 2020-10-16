# 36599776


def hasCycle(head):
    slow_node = head
    fast_node = head
    while True:
        if slow_node.next is None:
            return False
        slow_node = slow_node.next
        if fast_node.next is None or fast_node.next.next is None:
            return False
        fast_node = fast_node.next.next
        if slow_node is fast_node:
            return True
