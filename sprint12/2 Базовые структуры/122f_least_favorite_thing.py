class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        head = node.next_item
        return head

    head = node

    while idx-1:
        node = node.next_item
        idx -= 1

    if node.next_item.next_item is None:
        node.next_item = None
    elif node.next_item.next_item is not None:
        node.next_item = node.next_item.next_item
    return head
