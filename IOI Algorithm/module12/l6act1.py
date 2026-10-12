class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_nodes_with_one_child(root, single_child_nodes=None):
    if single_child_nodes is None:
        single_child_nodes = []

    if not root:
        return single_child_nodes

    # Check if the current node has exactly one child
    if (root.left and not root.right) or (root.right and not root.left):
        single_child_nodes.append(root)

    # Recurse on the left and right subtrees
    find_nodes_with_one_child(root.left, single_child_nodes)
    find_nodes_with_one_child(root.right, single_child_nodes)

    return single_child_nodes

def find_paths_in_range(root, low, high, current_path=None, current_sum=0, valid_paths=None):
    if valid_paths is None:
        valid_paths = []

    if current_path is None:
        current_path = []

    if root is None:
        return valid_paths

    # Include the current node in the path and add its value to the sum
    current_path.append(root.val)
    current_sum += root.val

    # If it's a leaf node, check if the current sum is within the range
    if root.left is None and root.right is None:
        if low <= current_sum <= high:
            # Append a copy of the current path to valid_paths
            valid_paths.append(list(current_path))
    else:
        # Recurse on the left and right children
        find_paths_in_range(root.left, low, high, current_path, current_sum, valid_paths)
        find_paths_in_range(root.right, low, high, current_path, current_sum, valid_paths)

    # Backtrack: Remove the current node before returning to the caller
    current_path.pop()

    return valid_paths

def main():
    # Construct the binary tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(7)
    root.right.left = Node(8)
    root.right.right = Node(6)

    # Find and collect nodes with exactly one child
    single_child_nodes = find_nodes_with_one_child(root)

    # Print nodes with exactly one child
    if not single_child_nodes:
        print(-1)
    else:
        print("Nodes with exactly one child:")
        for node in single_child_nodes:
            print(node.val, end=" ")
        print()

    # Define the sum range
    low = 14
    high = 21

    # Find and print all root-to-leaf paths within the sum range
    valid_paths = find_paths_in_range(root, low, high)
    if valid_paths:
        print(f"\nRoot-to-leaf paths with sum in range [{low}, {high}]:")
        for path in valid_paths:
            print(" -> ".join(map(str, path)))
    else:
        print(f"\nThere are no root-to-leaf paths with sum in range [{low}, {high}].")

if __name__ == "__main__":
    main()