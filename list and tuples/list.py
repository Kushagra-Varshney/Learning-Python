#list stores collection of items of any data type
#list is mutable
friends = ["Rolf", "Bob", "Anne", 1, 0.5]
print(friends)  # ['Rolf', 'Bob', 'Anne', 1, 0.5]

friends[0] = "Smith"
print(friends)  # ['Smith', 'Bob', 'Anne', 1, 0.5]

friends.append("John")
print(friends)  # ['Smith', 'Bob', 'Anne', 1, 0.5, 'John']

friends.remove("Bob")
print(friends)  # ['Smith', 'Anne', 1, 0.5, 'John']

friends.insert(2, "Alice")
print(friends)  # ['Smith', 'Anne', 'Alice', 1, 0.5, 'John']

friends.pop()
print(friends)  # ['Smith', 'Anne', 'Alice', 1, 0.5]

print(len(friends))  # 5