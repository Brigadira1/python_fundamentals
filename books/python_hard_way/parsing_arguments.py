from argparse import ArgumentParser

parser = ArgumentParser()
# parser.add_argument(
#     "echo",
#     help="Whatever argument the scripts receive, the argument name will be dispalyed on the screen.",
# )
# parser.add_argument("square", help="Calculate the square of a number.", type=int)
parser.add_argument("--verbosity", help="Show more info on the screen...")
args = parser.parse_args()
# print(args.square**2)
