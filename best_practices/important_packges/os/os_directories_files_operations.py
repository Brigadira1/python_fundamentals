import os

# Printing the current directory
print(os.getcwd())


# Function checking whether a directory is empty
def is_Empty(dir_path):
    return len(os.listdir(dir_path)) == 0


# Creating three sub-folders in the current directory
if not os.path.exists("Test_1"):
    os.makedirs("Test_1/Test2/Test_3")

# Prints all the files and directories in the current folder
print(os.listdir())


# Deletes a folder recursively if it exists
def delete_folders_recursively(dir_path):
    if len(os.listdir(dir_path)) == 0:
        os.rmdir(dir_path)

    else:


