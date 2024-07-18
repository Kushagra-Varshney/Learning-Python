str = "Hello world"
# Slice the string from index 0 to 5 , 5 is not included
print(str[0:5])  # Hello
print(str[6:11])  # world

#can also use negative indexes
print(str[-5:-1])  # worl

# str[:5] is equivalent to str[0:5]
# str[6:] is equivalent to str[6:11] (length)

#print with skip index
print(str[0:11:2]) # Hlowrd 2 indicates take every 2nd character