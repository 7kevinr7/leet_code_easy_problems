
from util.base_tester import BaseTester
from src.max_depth_bt import Solution as MaxDepthSolution
from util.tree_node import TreeNode


class Solution:

    @staticmethod
    def diameter_bt(root: TreeNode) -> int:
        # left max_depth + right max_depth
        if root is not None:
            return MaxDepthSolution.max_depth_bt(root.left) + MaxDepthSolution.max_depth_bt(root.right)

        return 0


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[1, 2, 3, 4, 5], [1, 2]]
        outputs = [3, 1]

        trees = list()

        tree1 = TreeNode(1)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(3)
        tree1.left.left = TreeNode(4)
        tree1.left.right = TreeNode(5)

        tree2 = TreeNode(1)
        tree2.left = TreeNode(2)

        trees.append(tree1)
        trees.append(tree2)

        return Tester.test_all(Solution.diameter_bt, trees, outputs, verbose)
