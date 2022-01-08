
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
    def test():
        inputs = [[3, 2, 0, -4, 2], [1, 2, 1], [1]]
        outputs = [True, True, False]

        for index in range(len(inputs)):
            head = Solution.build_linked_list(inputs[index])

            result = Solution.has_cycle(head)

            print(f"Test {index + 1} - {inputs[0] if outputs[index] == False else inputs[0][:-1]}: {outputs[index]} -> {result}")
            assert outputs[index] == result
