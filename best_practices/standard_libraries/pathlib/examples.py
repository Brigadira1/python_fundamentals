from pathlib import Path

# BASE_DIR = Path(__file__).parent
# blog_folder = BASE_DIR / "website" / "blog"
#
# # Creates the folder structure even if the parents don't exist yet!!!
# blog_folder.mkdir(parents=True, exist_ok=True)
#
# my_blog_post = blog_folder / "my_blog_post.txt"
# my_blog_post.write_text("TEEEEEEEEEEEEEEEEEEEST BLOG!!!!")
#
# # Creating a file and a directory
# folder = Path("MyFolder")
# folder.mkdir(exist_ok=True)
file = Path("myfile.txt")

# If the folder exists it will not throw an Exception
# folder.mkdir(exist_ok=True)

# Creates the file
file.touch()

# Renaming a file and folder
# folder.rmdir()
# folder.rename("NEW-FOLDER")
# file.rename("myfile.txt")

# Create a new file in a directory
# new_file = folder / "new_file.txt"
# new_file.touch()

# Writing text to file
# new_file.write_text("This is a test - repeat - this is a test!!")

# Creating multiple files and writing text to them
# current_folder = Path(".")
# for i in range(1, 6):
#     new_file = current_folder / f"new-file-{i}.txt"
#     new_file.touch()
#     new_file.write_text(f"New file: {i}.txt")

# Reading a file
# content = new_file.read_text()
# print(content)

# Full OS path to the current folder!!
# print(Path(".").resolve())

# Read files in a folder - Only in the current folder but not recursively
# for path in current_folder.iterdir():
#     print(path.name)

# Read files recursively in a folder showing all files and folders
# for path in current_folder.glob('**/*'):
#     print(path.name)

# Delete a specific type of file in a directory
# for path in current_folder.iterdir():
#     if 'new-file-' in path.name:
#         path.unlink()
#
# # Delete a single file
# Path("myfile.txt").unlink()

# Another way of representing the current directory of the file
# current_dir = Path(__file__).parent
# print(current_dir)

# Getting the file attributes
file_name = file.name
file_suffix = file.suffix
# File stem is the name of the file WITHOUT the extension/suffix
file_stem = file.stem
print(
      f"File name is {file_name}",
      f"File suffix is {file_suffix}",
      f"File stem is: {file.stem}", sep="\n"
      )

