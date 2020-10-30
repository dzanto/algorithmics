class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, elem):
    index = 0
    while node.next_item is not None:
        if node.value == elem:
            return index
        index += 1
        node = node.next_item
    if node.value == elem:
        return index
    else:
        return -1
