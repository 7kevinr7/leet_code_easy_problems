
from Easy.base_tester import BaseTester

class Solution:

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    @staticmethod
    def build_linked_list(nodes: list) -> ListNode:
        head = Solution.ListNode(nodes[0])
        temp_node = head
        for node in nodes[1:]:
            temp_node.next = Solution.ListNode(node)
            temp_node = temp_node.next

        return head

    @staticmethod
    def middle_node(head: ListNode) -> ListNode:
        values = list()
        temp_node = head

        while temp_node != None:
            values.append(temp_node.val)
            temp_node = temp_node.next

        return values[int(len(values)/2):]


class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]
        outputs = [[3, 4, 5], [4, 5, 6]]

        for index in range(len(inputs)):
            head = Solution.build_linked_list(inputs[index])

            result = Solution.middle_node(head)

            print(f"Test {index + 1} - {inputs[0]}: {outputs[index]} -> {result}")
            assert outputs[index] == result
