
from util.base_tester import BaseTester
from util.list_node import ListNode
from util.list_node import build_linked_list


class Solution:

    @staticmethod
    def palindrome(head: ListNode) -> ListNode:
        values = list()
        temp_node = head

        while temp_node != None:
            values.append(temp_node.val)
            temp_node = temp_node.next

        for index in range(len(values)):
            if values[index] != values[-(index + 1)]:
                return False

        return True


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[1, 2, 2, 1], [1, 2]]
        outputs = [True, False]

        passed_count = 0
        out_str = ""
        for index in range(len(inputs)):
            head = build_linked_list(inputs[index])

            result = Solution.palindrome(head)

            try:
                assert outputs[index] == result
                out_str += (f"Test {index + 1} - palindrome_linked_list: {inputs[0]}: {outputs[index]} -> {result}: Passed") + "\n"
                passed_count += 1
            except AssertionError as e:
                out_str += (f"Test {index + 1} - palindrome_linked_list: {inputs[0]}: {outputs[index]} -> {result}: Failed") + "\n"

        BaseTester.print_results(Solution.palindrome, out_str, passed_count, len(inputs), verbose)
