
from util.base_tester import BaseTester
from util.tree_node import TreeNode


class Solution:

    @staticmethod
    def same_tree(root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is not None:
            return False
        elif root1 is not None and root2 is None:
            return False
        elif root1 is None and root2 is None:
            return True

        if root1.val != root2.val:
            return False

        if not Solution.same_tree(root1.left, root2.left):
            return False

        if not Solution.same_tree(root1.right, root2.right):
            return False

        return True


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[[1, 2, 3], [1, 2, 3]], [[1, 2], [1, None, 2]]]
        outputs = [True, False]

        trees = list()
        tree1 = TreeNode(inputs[0][0][0])
        tree1.left = TreeNode(inputs[0][0][1])
        tree1.right = TreeNode(inputs[0][0][2])

        tree2 = TreeNode(inputs[0][1][0])
        tree2.left = TreeNode(inputs[0][1][1])
        tree2.right = TreeNode(inputs[0][1][2])

        tree3 = TreeNode(inputs[1][0][0])
        tree3.left = TreeNode(inputs[1][0][1])

        tree4 = TreeNode(inputs[1][1][0])
        tree4.left = TreeNode(inputs[1][1][1])
        tree4.right = TreeNode(inputs[1][1][2])

        trees.extend([[tree1, tree3], [tree2, tree4]])

        return Tester.test_all_multi_param(Solution.same_tree, trees, outputs, verbose)
