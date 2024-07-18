name = "Kushagra varshney"

# Returns the length of the string
print(len(name))  # 16

print(name.upper())  # KUSHAGRA VARSHNEY

print(name.lower())  # kushagra varshney

# Returns the index of the first occurrence of the substring
print(name.index("a"))  # 2

# Returns the count of the substring
print(name.count("a"))  # 3

# Returns the string with the first character capitalized
print(name.capitalize())  # Kushagra varshney

# Returns the string with the first character of each word capitalized
print(name.title())  # Kushagra Varshney

# Replace the substring with the new substring
print(name.replace("a", "A"))  # KushAgrA vArshney

# Returns the string with the leading and trailing characters removed
print(name.strip("K"))  # ushagra varshney

# Returns the string with the leading characters removed
print(name.lstrip("K"))  # ushagra varshney

# Returns the string with the trailing characters removed
print(name.rstrip("y"))  # Kushagra varshne