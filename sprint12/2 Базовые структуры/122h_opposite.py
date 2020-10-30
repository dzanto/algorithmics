class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node):
    while node.next is not None:
        tmp = node
        node = tmp.next

    head = DoubleConnectedNode(node.next.value, next=node.next.prev)
    return head
