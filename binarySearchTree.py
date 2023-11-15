class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def insert(self, node):
        if self.root:
            if node.data < self.root.data:
                if self.root.left is None:
                    self.root.left = node
                    self.root.left.parent = self.root
                else:
                    BinarySearchTree(self.root.left).insert(node)
            elif node.data > self.root.data:
                if self.root.right is None:
                    self.root.right = node
                    self.root.right.parent = self.root
                else:
                    BinarySearchTree(self.root.right).insert(node)
            else:
                self.root.data = node.data

    def search_node_by_value(self, value, root):
        if root:
            if root.data == value:
                return root
            elif value < root.data:
                if root.left is None:
                    return "node not found"
                else:
                    if value == root.left.data:
                        return root.left
                    else:
                        return self.search_node_by_value(value, root.left)
            elif value > root.data:
                if root.right is None:
                    return "node not found"
                else:
                    if value == root.right.data:
                        return root.right
                    else:
                        return self.search_node_by_value(value, root.right)

    def get_largest_node(self):
        if self.root.right is not None:
            return BinarySearchTree(self.root.right).get_largest_node()
        else:
            return self.root

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def delete_node(self, node):
        if node.left is None and node.right is None:
            # not have sub-tree
            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = None
                    node.parent = None
                else:
                    node.parent.right = None
                    node.parent = None
            else:
                # the node is root
                self.root = None
        elif node.left is None and node.right is not None:
            # only have right sub-tree
            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right

        if node.left is not None:
            # have left sub-tree
            left_tree = BinarySearchTree(node.left)
            largest_node_in_left = left_tree.get_largest_node()

            if largest_node_in_left == node.left:
                largest_node_in_left.right = node.right
                largest_node_in_left.parent = node.parent
                if node == node.parent.left:
                    node.parent.left = largest_node_in_left
                if node.parent is None:
                    # the node is root
                    self.root = largest_node_in_left
            else:
                if largest_node_in_left.parent.right == largest_node_in_left:
                    largest_node_in_left.parent.right = None
                largest_node_in_left.parent = node.parent
                largest_node_in_left.right = node.right
                largest_node_in_left.left = node.left
                if node.parent is None:
                    # the node is root
                    self.root = largest_node_in_left
                else:
                    node.parent.left = largest_node_in_left


for i in range(10000):
    root = TreeNode(27)
    node1 = TreeNode(14)
    node2 = TreeNode(10)
    node3 = TreeNode(35)
    node4 = TreeNode(19)
    node5 = TreeNode(31)
    node6 = TreeNode(42)
    node7 = TreeNode(5)
    node8 = TreeNode(12)
    node9 = TreeNode(13)

    bst = BinarySearchTree(root)
    bst.insert(node1)
    bst.insert(node2)
    bst.insert(node3)
    bst.insert(node4)
    bst.insert(node5)
    bst.insert(node6)
    bst.insert(node7)
    bst.insert(node8)
    bst.insert(node9)

    bst.delete_node(node1)

    bst.search_node_by_value(31, root)
    bst.inorderTraversal(root)
