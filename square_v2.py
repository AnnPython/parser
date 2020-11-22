import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument("square", type=int,
                    help="display a square of a given number")
                    
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")

parser.add_argument("-s", "--sqrt", action="store_false",
                    help="get square root")
                    
args = parser.parse_args()

if args.sqrt:
    answer = args.square**2
    mod = 'square'
else:
    answer = math.sqrt(args.square)
    mod = 'square root'

if args.verbose:
    print(f"the {mod} of {args.square} equals {answer}")
else:
    print(answer)
