
from util.base_tester import BaseTester
from util.tree_node import TreeNode


class Solution:

    @staticmethod
    def avg_of_levels(root: TreeNode) -> list:
        queue = list()
        averages = list()
        queue.append(root)

        while len(queue) > 0:
            sum = 0
            count = 0
            temp = list()

            while len(queue) > 0:
                node = queue.pop(0)
                sum += node.val
                count += 1

                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)

            queue = temp
            averages.append(sum / count)

        return averages


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[3, 9, 20, None, None, 15, 7], [3, 9, 20, 15, 7]]
        outputs = [[3.0, 14.5, 11.0], [3.0, 14.5, 11.0]]

        trees = list()
        root = TreeNode(inputs[0][0])
        root.left = TreeNode(inputs[0][1])
        root.right = TreeNode(inputs[0][2])
        root.right.left = TreeNode(inputs[0][5])
        root.right.right = TreeNode(inputs[0][6])

        trees.append(root)
        root = TreeNode(inputs[1][0])
        root.left = TreeNode(inputs[1][1])
        root.right = TreeNode(inputs[1][2])
        root.left.left = TreeNode(inputs[1][3])
        root.left.right = TreeNode(inputs[1][4])

        trees.append(root)

        #for tree in trees:
        #    TreeNode.print_tree(tree)

        return Tester.test_all(Solution.avg_of_levels, trees, outputs, verbose)
