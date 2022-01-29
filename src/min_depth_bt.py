
from util.base_tester import BaseTester
from util.tree_node import TreeNode


class Solution:

    @staticmethod
    def min_depth(root: TreeNode) -> int:
        if root is not None:
            if root.right is None and root.left is None:
                return 1

            if root.left is None:
                return Solution.min_depth(root.right) + 1

            if root.right is None:
                return Solution.min_depth(root.left) + 1

            if root.left is not None and root.right is not None:
                right = Solution.min_depth(root.right)
                left = Solution.min_depth(root.left)
                return right if right < left else left + 1

        return 0


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[3, 9, 20, None, None, 15, 7], [2, None, 3, None, 4, None, 5, None, 6]]
        outputs = [2, 5]

        trees = list()
        root = TreeNode(inputs[0][0])
        root.left = TreeNode(inputs[0][1])
        root.right = TreeNode(inputs[0][2])
        root.right.left = TreeNode(inputs[0][5])
        root.right.right = TreeNode(inputs[0][6])
        trees.append(root)

        root = TreeNode(inputs[1][0])
        root.right = TreeNode(inputs[1][2])
        root.right.right = TreeNode(inputs[1][4])
        root.right.right.right = TreeNode(inputs[1][6])
        root.right.right.right.right = TreeNode(inputs[1][8])
        trees.append(root)

        #for tree in trees:
        #    TreeNode.print_tree(tree)

        return Tester.test_all(Solution.min_depth, trees, outputs, verbose)
