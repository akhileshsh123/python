# Creating an empty set
b = set()
print(type(b))

# adding values to an empty set
b.add(4)
b.add(5)
# b.add(5) Adding a value repeatdly does not changes a set
b.add([(4,5,6)])

# b.add({4,5}) cannot add list or dictionary to sets

# Accessing Elements
print(b)
# Length of the set

# print(len(b)) Prints the length of this set
# Removal of an Item
# b.remove(5) remove 5 front set b
# b.remove(15) a throws an errorwhile trying to remove is (which is not present in the set) 
print(b)

print(b.pop())
print(b)