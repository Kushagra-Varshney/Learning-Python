# sets are unordered collections of unique elements
d = {} # empty dictionary
s = set() # empty set
# set with elements
s = {1, 2, 3, 4, 5, 5, 5, 5}
print(s)  # {1, 2, 3, 4, 5}

# Adding elements to a set
s.add(6)
print(s)  # {1, 2, 3, 4, 5, 6}

# Removing elements from a set
s.remove(3)
print(s)  # {1, 2, 4, 5, 6}

# Checking if an element is present in a set
print(2 in s)  # True
print(3 in s)  # False

# Getting the length of a set
print(len(s))  # 5

# Clearing all elements from a set
s.clear()
print(s)  # set()

# Copying a set
s = {1, 2, 3}
s_copy = s.copy()
print(s_copy)  # {1, 2, 3}

# Performing set operations
s1 = {1, 2, 3}
s2 = {3, 4, 5}
union = s1.union(s2)
intersection = s1.intersection(s2)
difference = s1.difference(s2)
print(union)  # {1, 2, 3, 4, 5}
print(intersection)  # {3}
print(difference)  # {1, 2}