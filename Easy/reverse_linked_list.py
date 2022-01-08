
from Easy.base_tester import BaseTester

class Solution:

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    @staticmethod
    def build_linked_list(nodes: list) -> ListNode:
        if len(nodes) == 0:
            return None
        head = Solution.ListNode(nodes[0])
        temp_node = head
        for node in nodes[1:]:
            temp_node.next = Solution.ListNode(node)
            temp_node = temp_node.next

        return head

    @staticmethod
    def reverse_list(head: ListNode) -> ListNode:
        if head is None:
            return []
        temp_node = head.next
        previous = head
        values = list()

        while temp_node != None:
            next = temp_node.next
            temp_node.next = previous
            previous = temp_node
            temp_node = next

        # return previous

        # for testing
        head.next = None
        temp_node = previous

        while temp_node != None:
            values.append(temp_node.val)
            temp_node = temp_node.next

        return values


class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[1, 2, 3, 4, 5], [1, 2], []]
        outputs = [[5, 4, 3, 2, 1], [2, 1], []]

        for index in range(len(inputs)):
            head = Solution.build_linked_list(inputs[index])

            result = Solution.reverse_list(head)

            print(f"Test {index + 1} - {inputs[0]}: {outputs[index]} -> {result}")
            assert outputs[index] == result
