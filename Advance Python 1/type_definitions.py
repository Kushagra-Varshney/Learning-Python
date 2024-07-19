from typing import List, Tuple, Dict

def calculate_average(numbers: List[int]) -> float:
    total = sum(numbers)
    average = total / len(numbers)
    return average

def get_user_info() -> Tuple[str, int, Dict[str, str]]:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    info = {
        "name": name,
        "age": str(age),
        "address": address
    }
    return (name, age, info)

# Example usage
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(f"The average is: {average}")

name, age, info = get_user_info()
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Address: {info['address']}")