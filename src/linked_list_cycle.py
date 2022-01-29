
from util.base_tester import BaseTester
from util.list_node import ListNode
from util.list_node import build_linked_list


class Solution:

    @staticmethod
    def has_cycle(head: ListNode) -> bool:
        temp_node = head.next
        visited = [head.val]

        while temp_node != None:
            if temp_node.val in visited:
                return True
            else:
                visited.append(temp_node.val)
            temp_node = temp_node.next

        return False


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[3, 2, 0, -4, 2], [1, 2, 1], [1]]
        outputs = [True, True, False]

        passed_count = 0
        out_str = ""
        for index in range(len(inputs)):
            head = build_linked_list(inputs[index])

            result = Solution.has_cycle(head)
            try:
                assert outputs[index] == result
                out_str += (f"Test {index + 1} - cycle_linked_list: {inputs[0] if outputs[index] == False else inputs[0][:-1]}: {outputs[index]} -> {result}: Passed") + "\n"
                passed_count += 1
            except AssertionError as e:
                out_str += (f"Test {index + 1} - cycle_linked_list: {inputs[0] if outputs[index] == False else inputs[0][:-1]}: {outputs[index]} -> {result}: Failed") + "\n"

        BaseTester.print_results(Solution.has_cycle, out_str, passed_count, len(inputs), verbose)
