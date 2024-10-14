import shutil
import sys

from rich import print

print("[bold magenta]Hello, this is a test using the rich library![/bold magenta]")
print(sys.executable)
print(f"Python path is: {shutil.which("python")}")
