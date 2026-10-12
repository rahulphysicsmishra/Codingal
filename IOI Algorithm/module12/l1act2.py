tree = [None] * 10  # Initial size

def ensure_capacity(index):
    """Ensure the tree array has enough capacity."""
    if index >= len(tree):
        # Extend the tree size
        new_size = max(index + 1, len(tree) * 2)
        tree.extend([None] * (new_size - len(tree)))

def root(key):
    if tree[0] is not None:
        print("Tree already has a root")
    else:
        tree[0] = key

def set_left(key, parent):
    child_index = (parent * 2) + 1
    if parent >= len(tree) or tree[parent] is None:
        print(f"Can't set left child at index {child_index}, no parent found at index {parent}")
    else:
        ensure_capacity(child_index)
        tree[child_index] = key

def set_right(key, parent):
    child_index = (parent * 2) + 2
    if parent >= len(tree) or tree[parent] is None:
        print(f"Can't set right child at index {child_index}, no parent found at index {parent}")
    else:
        ensure_capacity(child_index)
        tree[child_index] = key

def print_tree():
    for i, value in enumerate(tree):
        if value is not None:
            print(f"{value} ", end="")
        else:
            print("- ", end="")
    print()

# Example usage
root('A')
set_left('B', 0)
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_left('F', 2)
set_right('G', 2)
set_left('H', 3)
set_right('I', 3)
print_tree()



#optional
def print_tree_visual(index, indent=0):
    if index < len(tree) and tree[index] is not None:
        print_tree_visual((index * 2) + 2, indent + 4)
        print(" " * indent + str(tree[index]))
        print_tree_visual((index * 2) + 1, indent + 4)


print("Visual Representation of the Binary Tree:")
print_tree_visual(0)
