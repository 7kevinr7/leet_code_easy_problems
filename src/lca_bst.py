
from util.base_tester import BaseTester
from util.tree_node import TreeNode


class Solution:

    @staticmethod
    def lca_bst(root1: TreeNode, node1: TreeNode, node2: TreeNode) -> TreeNode:
        lca = None
        if root1 is not None:
            node1_left = TreeNode.dfs(root1.left, node1)
            node2_left = TreeNode.dfs(root1.left, node2)

            # nodes split, this is the lca
            if node1_left != node2_left or root1.val == node1.val or root1.val == node2.val:
                lca = TreeNode(root1.val)
            # both nodes are on the left, traverse to left
            elif node1_left and node2_left:
                lca = Solution.lca_bst(root1.left, node1, node2)
            # both nodes are on the right, traverse to right
            elif not node1_left and not node2_left:
                lca = Solution.lca_bst(root1.right, node1, node2)

        return lca


class Tester(BaseTester):

    @staticmethod
    def test(verbose=False):
        inputs = [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], [2, 1], [2, 8], [2, 4], [2, 1]]
        outputs = [[3, 4, 5, 5, 4, None, 7], [2, 2]]

        parameters = list()

        tree1 = TreeNode(6)
        tree1.left = TreeNode(2)
        tree1.right = TreeNode(8)
        tree1.left.left = TreeNode(0)
        tree1.left.right = TreeNode(4)
        tree1.right.left = TreeNode(7)
        tree1.right.right = TreeNode(9)
        tree1.left.right.left = TreeNode(3)
        tree1.left.right.right = TreeNode(5)

        tree2 = TreeNode(2)
        tree2.left = TreeNode(1)

        parameters.append([tree1, tree1, tree2])
        parameters.append([TreeNode(2), TreeNode(2), TreeNode(2)])
        parameters.append([TreeNode(8), TreeNode(4), TreeNode(1)])

        out_nodes = list()
        out_nodes.append(TreeNode(6))
        out_nodes.append(TreeNode(2))
        out_nodes.append(TreeNode(2))

        return Tester.test_all_multi_param(Solution.lca_bst, parameters, out_nodes, verbose)
