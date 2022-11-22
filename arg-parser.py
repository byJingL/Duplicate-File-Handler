import argparse

# ------------------ optional arguments -------------- #
# Can assign arg or can't
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", help="Input test number")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
print(args.test)
if args.verbose:
    print("verbosity turned on")

# ------------------ positional arguments -------------- #
parser = argparse.ArgumentParser()
parser.add_argument('test_arg', help='Input your test number after file.py', type=int)
args = parser.parse_args()
print(args.test_arg ** 2)


# ------------------ combination of two -------------- #
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="A num to be make a square of it")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="A num to be make a square of it")
parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print(f"the square of {args.square} equals {answer}")
elif args.verbosity == 1:
    print(f"{args.square}^2 == {answer}")
else:
    print(answer)