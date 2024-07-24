# List Operations
print("List Operations:")
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Append
my_list.append(6)
print("After append:", my_list)

# Extend
my_list.extend([7, 8])
print("After extend:", my_list)

# Insert
my_list.insert(2, 'a')
print("After insert:", my_list)

# Remove
my_list.remove('a')
print("After remove:", my_list)

# Pop
popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After pop:", my_list)

# Index
index_of_element = my_list.index(4)
print("Index of 4:", index_of_element)

# Count
count_of_element = my_list.count(5)
print("Count of 5:", count_of_element)

# Sort
my_list.sort()
print("After sort:", my_list)

# Reverse
my_list.reverse()
print("After reverse:", my_list)

# Copy
list_copy = my_list.copy()
print("List copy:", list_copy)

# Clear
my_list.clear()
print("After clear:", my_list)

# Tuple Operations
print("\nTuple Operations:")
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

# Index
index_of_element = my_tuple.index(3)
print("Index of 3:", index_of_element)

# Count
count_of_element = my_tuple.count(2)
print("Count of 2:", count_of_element)

# Convert list to tuple
list_to_tuple = tuple([1, 2, 3, 4])
print("List to tuple:", list_to_tuple)

# Sets Operations
print("\nSet Operations:")
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Add
my_set.add(6)
print("After add:", my_set)

# Update
my_set.update([7, 8])
print("After update:", my_set)

# Remove
my_set.remove(2)
print("After remove:", my_set)

# Discard
my_set.discard(10)  # No error even if element is not present
print("After discard:", my_set)

# Pop
popped_element = my_set.pop()
print("Popped element:", popped_element)
print("After pop:", my_set)

# Clear
my_set.clear()
print("After clear:", my_set)

# Additional Set Methods
print("\nAdditional Set Methods:")
another_set = {1, 2, 3, 4, 5}
print("Another set:", another_set)

# Union
union_set = my_set.union(another_set)
print("Union:", union_set)

# Intersection
intersection_set = my_set.intersection(another_set)
print("Intersection:", intersection_set)

# Difference
difference_set = my_set.difference(another_set)
print("Difference:", difference_set)

# Symmetric Difference
sym_diff_set = my_set.symmetric_difference(another_set)
print("Symmetric Difference:", sym_diff_set)

# Copy
set_copy = another_set.copy()
print("Set copy:", set_copy)

# Discard (with no error if item does not exist)
another_set.discard(10)
print("After discard:", another_set)

# Remove (raises KeyError if item does not exist)
try:
    another_set.remove(10)
except KeyError:
    print("Item 10 not found for remove")

# Dictionary Operations
print("\nDictionary Operations:")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", my_dict)

# Get
value = my_dict.get('b')
print("Value for 'b':", value)

# Setdefault
value = my_dict.setdefault('d', 4)
print("After setdefault:", my_dict)

# Update
my_dict.update({'e': 5, 'f': 6})
print("After update:", my_dict)

# Pop
popped_item = my_dict.pop('c')
print("Popped item:", popped_item)
print("After pop:", my_dict)

# Popitem
key, value = my_dict.popitem()
print("Popped item:", key, value)
print("After popitem:", my_dict)

# Keys
keys = my_dict.keys()
print("Keys:", keys)

# Values
values = my_dict.values()
print("Values:", values)

# Items
items = my_dict.items()
print("Items:", items)

# Clear
my_dict.clear()
print("After clear:", my_dict)

# Additional Dictionary Methods
print("\nAdditional Dictionary Methods:")

# Copy
dict_copy = my_dict.copy()
print("Dictionary copy:", dict_copy)

# Fromkeys
default_dict = dict.fromkeys(['a', 'b', 'c'], 0)
print("Fromkeys:", default_dict)

# Setdefault (already demonstrated above)
# Del
del dict_copy
print("After deleting dict_copy, it no longer exists")

# Conversion to Dictionary from a List of Tuples
list_of_tuples = [('a', 1), ('b', 2)]
converted_dict = dict(list_of_tuples)
print("List of tuples to dictionary:", converted_dict)
