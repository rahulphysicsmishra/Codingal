class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def print_k_distance_node_down(root, k):
	"""
	Prints all nodes at distance k below the given root.
	"""
	if root is None or k < 0:
		return

	if k == 0:
		print(root.data, end=' ')
		return

	print_k_distance_node_down(root.left, k-1)
	print_k_distance_node_down(root.right, k-1)

def print_k_distance_node(root, target, k):
	"""
	Prints all nodes at distance k from the target node.
	"""
	if root is None:
		return -1

	if root == target:
		print(f"Nodes at distance {k} from target {target.data}:")
		print_k_distance_node_down(root, k)
		return 0

	# Check in left subtree
	dl = print_k_distance_node(root.left, target, k)

	if dl != -1:
		if dl + 1 == k:
			print(root.data, end=' ')
		else:
			print_k_distance_node_down(root.right, k - dl - 2)
		return 1 + dl

	# Check in right subtree
	dr = print_k_distance_node(root.right, target, k)
	if dr != -1:
		if dr + 1 == k:
			print(root.data, end=' ')
		else:
			print_k_distance_node_down(root.left, k - dr - 2)
		return 1 + dr

	return -1

def main():
	# Construct the binary tree
	root = Node(20)
	root.left = Node(8)
	root.right = Node(22)
	root.left.left = Node(4)
	root.left.right = Node(12)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)

	target = root.left.right  # Node with data 12
	k = 2

	# print(f"Nodes at distance {k} from target node {target.data}:")
	# print()
	print_k_distance_node(root, target, k)
	print()  # For a newline after the output

if __name__ == "__main__":
	main()
