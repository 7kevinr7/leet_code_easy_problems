
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
    def remove_element(head: ListNode, target: int) -> ListNode:
        new_list = list()
        temp_node = head

        while temp_node != None:
            if temp_node.val != target:
                new_list.append(temp_node.val)

            temp_node = temp_node.next

        # Solution.build_linked_list(new_list)
        return new_list

class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[[1, 2, 6, 3, 4, 5, 6], 6], [[], 1], [[7, 7, 7, 7], 7]]
        outputs = [[1, 2, 3, 4, 5], [], []]

        for index in range(len(inputs)):
            head = Solution.build_linked_list(inputs[index][0])

            result = Solution.remove_element(head, inputs[index][1])

            print(f"Test {index + 1} - {inputs[0]}: {outputs[index]} -> {result}")
            assert outputs[index] == result
