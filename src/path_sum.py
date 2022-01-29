
from util.base_tester import BaseTester
from util.tree_node import TreeNode


class Solution:

    @staticmethod
    def has_path_sum(root: TreeNode, target_sum: int) -> bool:
        if root is None:
            return False

        if TreeNode.is_leaf(root) and target_sum == root.val:
            return True

        if Solution.has_path_sum(root.right, target_sum - root.val):
            return True
        if Solution.has_path_sum(root.left, target_sum - root.val):
            return True

        return False


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], [1, 2, 3], []], [22, 5, 0]]
        outputs = [True, False, False]

        parameters = list()

        tree1 = TreeNode(5)
        tree1.left = TreeNode(4)
        tree1.right = TreeNode(8)
        tree1.left.left = TreeNode(11)
        tree1.right.left = TreeNode(13)
        tree1.right.right = TreeNode(4)
        tree1.left.left.left = TreeNode(7)
        tree1.left.left.right = TreeNode(2)
        tree1.right.right.right = TreeNode(1)

        tree2 = TreeNode(1)
        tree2.left = TreeNode(2)
        tree2.right = TreeNode(3)

        tree3 = None

        parameters.append([tree1, tree2, tree3])
        parameters.append(inputs[1])

        return Tester.test_all_multi_param(Solution.has_path_sum, parameters, outputs, verbose)
