b_tree_node = [10, 20, 30, 40, 50]

key = int(input("Enter number to insert: "))

inserted = False
for i in range(len(b_tree_node)):
    if key < b_tree_node[i]:
        b_tree_node.insert(i, key)
        inserted = True
        break

if not inserted: 
    b_tree_node.append(key)

print("Updated B-Tree node: ", b_tree_node)