# Define a global variable
global_var = 10

# Function to modify the global variable
def modify_global():
    global global_var
    global_var = 20

# Access the global variable
print("Global variable:", global_var)

# Modify the global variable
modify_global()

# Access the modified global variable
print("Modified global variable:", global_var)