
from util.base_tester import BaseTester
from util.tree_node import TreeNode
from copy import deepcopy


class Solution:

    @staticmethod
    def subtree_another_tree(root1: TreeNode, sub_root: TreeNode) -> bool:
        pass


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[3, 4, 5, 1, 2], [3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], [4, 1, 2]]
        outputs = [True, False]

        parameters = list()

        tree1 = TreeNode(3)
        tree1.left = TreeNode(4)
        tree1.right = TreeNode(5)
        tree1.left.left = TreeNode(1)
        tree1.left.right = TreeNode(2)

        tree2 = TreeNode(4)
        tree2.left = TreeNode(1)
        tree2.right = TreeNode(2)

        tree3 = deepcopy(tree1)
        tree3.left.right.left = TreeNode(0)

        parameters.append([tree1, tree3])
        parameters.append([tree2, tree2])

        return Tester.test_all_multi_param(Solution.subtree_another_tree, parameters, outputs, verbose)
