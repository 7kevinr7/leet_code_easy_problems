
from util.base_tester import BaseTester
from util.tree_node import TreeNode


class Solution:

    @staticmethod
    def max_depth_bt(root: TreeNode) -> int:
        if root is not None:
            left_depth = Solution.max_depth_bt(root.left) + 1
            right_depth = Solution.max_depth_bt(root.right) + 1

            return left_depth if left_depth > right_depth else right_depth

        return 0


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[3, 9, 20, None, None, 15, 7], [1, None, 2]]
        outputs = [3, 2]

        trees = list()

        tree1 = TreeNode(3)
        tree1.left = TreeNode(9)
        tree1.right = TreeNode(20)
        tree1.right.left = TreeNode(15)
        tree1.right.right = TreeNode(7)

        tree2 = TreeNode(1)
        tree2.right = TreeNode(2)

        trees.append(tree1)
        trees.append(tree2)

        return Tester.test_all(Solution.max_depth_bt, trees, outputs, verbose)
