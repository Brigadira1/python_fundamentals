import sys

sys.stdout.write("\n")
sys.stdout.write(sys.platform)
sys.stdout.write("\n" + str(sys.version_info))
sys.stdout.write("\n" + sys.version)
sys.stdout.write("\n" + str(sys.argv))  # You can reference the arguments passed to the command line
sys.stdout.write("\n" + str(sys.builtin_module_names))
sys.stdout.write("\n" + str(sys.executable))
sys.stdout.write("\n" + str(sys.getwindowsversion()))
sys.stderr.write("\n The text that you see is red and will be printed before the out statements!!!!")
