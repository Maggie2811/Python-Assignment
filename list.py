# Create an empty list
my_list = []
#print("my_list")

# Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#print("After Append:", my_list)

# Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
#print(my_list[1])

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50,60,70])
#print("List after append:", my_list )

# Remove the last element from my_list
my_list.pop(-1)
#print(my_list)

# Sort my_list in ascending order
my_list.sort()
#print(my_list)

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# To view the final list (optional)
print("Final my_list:", my_list)