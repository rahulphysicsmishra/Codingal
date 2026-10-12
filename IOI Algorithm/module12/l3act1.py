class Node:
    """
    A class representing a node in a binary tree.

    Attributes:
    data: The value stored in the node.
    left_child: A reference to the left child node.
    right_child: A reference to the right child node.
    """

    def __init__(self, data):
        self.left_child = None
        self.data = data
        self.right_child = None

def find_size_recursive(root):
    """
    Calculates the total number of nodes in the binary tree recursively.

    Args:
    root (Node): The root node of the binary tree.

    Returns:
    int: The size of the binary tree.
    """

    if root is None:
        return 0

    return find_size_recursive(root.left_child) + find_size_recursive(root.right_child) + 1

def find_size_iterative(root):
    """
    Calculates the total number of nodes in the binary tree iteratively.

    Args:
    root (Node): The root node of the binary tree.

    Returns:
    int: The size of the binary tree.
    """

    if root is None:
        return 0

    count = 0
    stack = []
    stack.append(root)

    while stack:
        node = stack.pop()
        count += 1

        # Push left and right children onto the stack if they exist
        if node.left_child is not None:
            stack.append(node.left_child)
        if node.right_child is not None:
            stack.append(node.right_child)

    return count

# Constructing the binary tree
root = Node(1)
root.left_child = Node(2)
root.right_child = Node(3)
root.left_child.left_child = Node(4)
root.left_child.right_child = Node(5)
root.right_child.left_child = Node(6)
root.right_child.right_child = Node(7)
root.right_child.left_child.left_child = Node(8)
root.right_child.left_child.right_child = Node(9)

# Calculating and printing the size of the binary tree using recursive method
size_recursive = find_size_recursive(root)
print(f"The size of the binary tree (recursive) is: {size_recursive}")

# Calculating and printing the size of the binary tree using iterative method
size_iterative = find_size_iterative(root)
print(f"The size of the binary tree (iterative) is: {size_iterative}")