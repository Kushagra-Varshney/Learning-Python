# Dictionary is a collection of key-value pairs. It is unordered, changeable and indexed.

marks = {
    "Math": 90,
    "Science": 80,
    "English": 70,
    "list": [1, 2, 3]
}

print(marks)  # {'Math': 90, 'Science': 80, 'English': 70}
print(type(marks))  # <class 'dict'>
print(marks.keys())  # dict_keys(['Math', 'Science', 'English'])
print(marks.values())  # dict_values([90, 80, 70])

# marks["keynotpresent"] - using this will throw an error
print(marks.get("keynotpresent"))  # None - using this will not throw an error
# remove an item
marks.pop("list")
print(marks)  # {'Math': 90, 'Science': 80, 'English': 70}