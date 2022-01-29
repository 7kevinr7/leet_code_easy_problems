

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list(nodes: list) -> ListNode:
    if len(nodes) == 0:
        return None

    head = ListNode(nodes[0])
    temp_node = head
    for node in nodes[1:]:
        temp_node.next = ListNode(node)
        temp_node = temp_node.next

    return head
