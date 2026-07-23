b_tree_node = [10, 20, 30, 40, 50]
key = int(input("Enter the key to delete: "))
deleted = False
for i in range(len(b_tree_node)):
    if key == b_tree_node[i]:
        b_tree_node.pop(i)
        deleted = True
        break
if not deleted:
    print("Output: \n Entered element (key) not found in the B-Tree node!")
else:
    print("Output: \n Updated B-Tree node: 11", b_tree_node)