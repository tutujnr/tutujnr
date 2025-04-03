# Step 1: Create an empty list
my_list = []

# Step 2: Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position)
my_list.insert(1, 15)

# Step 4: Extend my_list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort my_list in ascending order
my_list.sort()

# Step 7: Find and print the index of value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# Print final list
print("Final List:", my_list)
