
from util.base_tester import BaseTester
from util.list_node import ListNode
from util.list_node import build_linked_list


class Solution:

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
    def test(verbose=False):
        inputs = [[1, 2, 3, 4, 5], [1, 2], []]
        outputs = [[5, 4, 3, 2, 1], [2, 1], []]

        passed_count = 0
        out_str = ""
        for index in range(len(inputs)):
            head = build_linked_list(inputs[index])

            result = Solution.reverse_list(head)

            try:
                assert outputs[index] == result
                out_str += (f"Test {index + 1} - reverse_linked_list: {inputs[0]}: {outputs[index]} -> {result}: Passed") + "\n"
                passed_count += 1
            except AssertionError as e:
                out_str += (f"Test {index + 1} - reverse_linked_list: {inputs[0]}: {outputs[index]} -> {result}: Failed") + "\n"

        BaseTester.print_results(Solution.reverse_list, out_str, passed_count, len(inputs), verbose)
