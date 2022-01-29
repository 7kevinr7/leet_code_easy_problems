

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def print_tree(root):
        if root is not None:
            print(root.val)
            TreeNode.print_tree(root.left)
            TreeNode.print_tree(root.right)

    @staticmethod
    def is_leaf(root):
        if root is not None and root.left is None and root.right is None:
            return True

        return False

    @staticmethod
    def dfs(root, target, visited=None):
        if root is not None:
            if visited is not None:
                visited.append(root.val)

            if root.val == target.val:
                return True
            if TreeNode.dfs(root.left, target, visited):
                return True
            if TreeNode.dfs(root.right, target, visited):
                return True

        return False

    def __str__(self):
        tree_str = str(self.val)
        if self.left is not None:
            tree_str += ", " + str(self.left)
        if self.right is not None:
            tree_str += ", " + str(self.right)

        return tree_str

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False

        if str(self) != str(other):
            return False

        return True
