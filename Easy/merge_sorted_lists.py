
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
    def merge_lists(head1: ListNode, head2: ListNode) -> ListNode:
        temp_node1 = head1
        temp_node2 = head2
        merge_list = []

        while temp_node1 is not None and temp_node2 is not None:
            if temp_node1.val <= temp_node2.val:
                merge_list.append(temp_node1.val)
                temp_node1 = temp_node1.next
            else:
                merge_list.append(temp_node2.val)
                temp_node2 = temp_node2.next

        while temp_node1 is not None:
            merge_list.append(temp_node1.val)
            temp_node1 = temp_node1.next
        while temp_node2 is not None:
            merge_list.append(temp_node2.val)
            temp_node2 = temp_node2.next

        return merge_list

class Tester(BaseTester):

    @staticmethod
    def test():
        inputs = [[[1, 2, 4], [1, 3, 4]], [[], []], [[], [0]]]
        outputs = [[1, 1, 2, 3, 4, 4], [], [0]]

        for index in range(len(inputs)):
            head1 = Solution.build_linked_list(inputs[index][0])
            head2 = Solution.build_linked_list(inputs[index][1])

            result = Solution.merge_lists(head1, head2)

            print(f"Test {index + 1} - {inputs[index][0]} + {inputs[index][1]}: {outputs[index]} -> {result}")
            assert outputs[index] == result
