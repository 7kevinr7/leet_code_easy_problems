
from util.base_tester import BaseTester
from util.list_node import ListNode
from util.list_node import build_linked_list


class Solution:

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
    def test(verbose=False):
        inputs = [[[1, 2, 6, 3, 4, 5, 6], 6], [[], 1], [[7, 7, 7, 7], 7]]
        outputs = [[1, 2, 3, 4, 5], [], []]

        passed_count = 0
        out_str = ""
        for index in range(len(inputs)):
            head = build_linked_list(inputs[index][0])

            result = Solution.remove_element(head, inputs[index][1])

            try:
                assert outputs[index] == result
                out_str += (f"Test {index + 1} - remove_linked_list: {inputs[0]}: {outputs[index]} -> {result}: Passed") + "\n"
                passed_count += 1
            except AssertionError as e:
                out_str += (f"Test {index + 1} - remove_linked_list: {inputs[0]}: {outputs[index]} -> {result}: Failed") + "\n"

        BaseTester.print_results(Solution.remove_element, out_str, passed_count, len(inputs), verbose)
