
from util.base_tester import BaseTester
from util.list_node import ListNode
from util.list_node import build_linked_list


class Solution:

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
    def test(verbose=False):
        inputs = [[1, 1, 2], [1, 1, 2, 3, 3]]
        outputs = [[1, 2], [1, 2, 3]]

        passed_count = 0
        out_str = ""
        for index in range(len(inputs)):
            head = build_linked_list(inputs[index])

            result = Solution.remove_duplicates(head)

            try:
                assert outputs[index] == result
                out_str += (f"Test {index + 1} - rm_duplicates_list: {inputs[0]}: {outputs[index]} -> {result}: Passed") + "\n"
                passed_count += 1
            except AssertionError as e:
                out_str += (f"Test {index + 1} - rm_duplicates_list: {inputs[0]}: {outputs[index]} -> {result}: Failed") + "\n"

        BaseTester.print_results(Solution.remove_duplicates, out_str, passed_count, len(inputs), verbose)

