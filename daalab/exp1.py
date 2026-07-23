b_tree_node = [10, 20, 30, 40, 50]

key = int(input("Enter a number to search: "))

found = False

for k in b_tree_node: 
    if k == key: 
        found = True
        break

if found: 
    print("Output; \n Entered element (key) found in the B-Tree node!")
else: 
    print("Output; \n Entered element (key) is not found in the B-Tree node!")