# This exercise is from the Real Python youtube channel: https://www.youtube.com/watch?v=8KHn7J7MSOo

from pathlib import Path

my_folder = Path(__file__).parent / "my_folder"
my_folder.mkdir(exist_ok=True)

file1 = my_folder / "file1.txt"
file1.touch()
file2 = my_folder / "file2.txt"
file2.touch()
png_file = my_folder / "image1.png"
png_file.touch()

images_folder = my_folder / "images"
images_folder.mkdir(exist_ok=True)

# png_file.rename(images_folder / f"{png_file.name}")
# This is similar to the rename method
png_file.replace(images_folder / "image1.png")
file1.unlink()

# for path in my_folder.glob("**/*"):
#     if path.is_file():
#         print(f"File to be deleted: {path.name}")
#         path.unlink()
#
# images_folder.rmdir()
# my_folder.rmdir()