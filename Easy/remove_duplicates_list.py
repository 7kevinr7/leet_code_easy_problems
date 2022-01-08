
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
    def remove_duplicates(head: ListNode) -> ListNode:
        seen = list()
        temp_node = head

        while temp_node != None and temp_node.next != None:
            if temp_node.next.val not in seen:
                seen.append(temp_node.next.val)
            else:
                temp_node.next = temp_node.next.next

            temp_node = temp_node.next

        return seen


class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[1, 1, 2], [1, 1, 2, 3, 3]]
        outputs = [[1, 2], [1, 2, 3]]

        for index in range(len(inputs)):
            head = Solution.build_linked_list(inputs[index])

            result = Solution.remove_duplicates(head)

            print(f"Test {index + 1} - {inputs[0]}: {outputs[index]} -> {result}")
            assert outputs[index] == result
