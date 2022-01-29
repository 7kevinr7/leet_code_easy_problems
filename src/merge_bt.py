
from util.base_tester import BaseTester
from util.tree_node import TreeNode


class Solution:

    @staticmethod
    def merge_bt(root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is not None and root2 is not None:
            temp_node = TreeNode(root1.val + root2.val)
            temp_node.left = Solution.merge_bt(root1.left, root2.left)
            temp_node.right = Solution.merge_bt(root1.right, root2.right)

            return temp_node
        elif root1 is None and root2 is not None:
            return root2
        elif root1 is not None and root2 is None:
            return root1

        return None


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [1], [1, 2]]
        outputs = [[3, 4, 5, 5, 4, None, 7], [2, 2]]

        trees = list()

        tree1 = TreeNode(1)
        tree1.left = TreeNode(3)
        tree1.right = TreeNode(2)
        tree1.left.left = TreeNode(5)

        tree2 = TreeNode(2)
        tree2.left = TreeNode(1)
        tree2.right = TreeNode(3)
        tree2.left.right = TreeNode(4)
        tree2.right.right = TreeNode(7)

        tree3 = TreeNode(1)

        tree4 = TreeNode(1)
        tree4.left = TreeNode(2)

        trees.append([tree1, tree3])
        trees.append([tree2, tree4])

        out_trees = list()

        tree5 = TreeNode(3)
        tree5.left = TreeNode(4)
        tree5.right = TreeNode(5)
        tree5.left.left = TreeNode(5)
        tree5.left.right = TreeNode(4)
        tree5.right.right = TreeNode(7)

        tree6  = TreeNode(2)
        tree6.left = TreeNode(2)

        out_trees.append(tree5)
        out_trees.append(tree6)

        return Tester.test_all_multi_param(Solution.merge_bt, trees, out_trees, verbose)
