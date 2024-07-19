import os

def create_file(file_path):
    try:
        with open(file_path, 'w') as file:
            print(f"File '{file_path}' created successfully.")
    except IOError:
        print(f"Error creating file '{file_path}'.")

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(f"Content of file '{file_path}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print(f"Content written to file '{file_path}' successfully.")
    except IOError:
        print(f"Error writing to file '{file_path}'.")

def append_file(file_path, content):
    try:
        with open(file_path, 'a') as file:
            file.write(content)
            print(f"Content appended to file '{file_path}' successfully.")
    except IOError:
        print(f"Error appending to file '{file_path}'.")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error deleting file '{file_path}'.")


file_path = 'file2.txt'
# create_file(file_path)
# write_file(file_path, 'Hello, World!')
# read_file(file_path)
# append_file(file_path, '\nPython is awesome!')
# read_file(file_path)

delete_file(file_path)