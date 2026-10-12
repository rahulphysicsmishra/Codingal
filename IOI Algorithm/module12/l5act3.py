class Node:
    def __init__(self, data):
        # Initializes a new Node with the given data and no children.
        self.data = data
        self.left = None
        self.right = None

def has_path_sum(node, target_sum):
    # Determines if the binary tree has a root-to-leaf path with the given sum.

    # Base Case: If the current node is None, no path exists
    if node is None:
        return False

    # Subtract the node's data from the target sum
    remaining_sum = target_sum - node.data

    # If the node is a leaf, check if the remaining sum is zero
    if remaining_sum == 0 and node.left is None and node.right is None:
        return True

    # Recurse on the left and right subtrees
    return has_path_sum(node.left, remaining_sum) or \
           has_path_sum(node.right, remaining_sum)

def find_paths_in_range(node, low, high, current_path=None, current_sum=0, valid_paths=None):
    # Finds all root-to-leaf paths where the sum of the node values is within [low, high].

    if valid_paths is None:
        valid_paths = []

    if current_path is None:
        current_path = []

    if node is None:
        return valid_paths

    # Include the current node in the path and add its value to the sum
    current_path.append(node.data)
    current_sum += node.data

    # If it's a leaf node, check if the current sum is within the range
    if node.left is None and node.right is None:
        if low <= current_sum <= high:
            # Append a copy of the current path to valid_paths
            valid_paths.append(list(current_path))
    else:
        # Recurse on the left and right children
        find_paths_in_range(node.left, low, high, current_path,
                           current_sum, valid_paths)
        find_paths_in_range(node.right, low, high, current_path,
                           current_sum, valid_paths)

    # Backtrack: Remove the current node before returning to the caller
    current_path.pop()

    return valid_paths

def main():
    """
    Constructs the binary tree and checks for root-to-leaf paths with sums
    in a specified range.
    """
    # Define the target sum for existence check
    target_sum = 21

    # Construct the binary tree
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(5)
    root.right.left = Node(2)

    # Check if there exists a root-to-leaf path with the target sum
    if has_path_sum(root, target_sum):
        print(f"There is at least one root-to-leaf path with sum {target_sum}.")
    else:
        print(f"There is no root-to-leaf path with sum {target_sum}.")

    # Define the sum range
    low = 14
    high = 21

    # Find and print all paths within the sum range
    paths = find_paths_in_range(root, low, high)
    if paths:
        print(f"\nRoot-to-leaf paths with sum in range [{low}, {high}]:")
        for path in paths:
            print(" -> ".join(map(str, path)))
    else:
        print(f"\nThere are no root-to-leaf paths with sum in range [{low}, {high}].")

if __name__ == "__main__":
    main()