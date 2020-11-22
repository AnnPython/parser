import argparse
import math

parser = argparse.ArgumentParser()


parser.add_argument("square", type=int,
                    help="display a square of a given number")
                    
parser.add_argument("-v", "--verbosity", action = "count",
                    help="increase output verbosity")

parser.add_argument("-s", "--sqrt", action="store_false",
                    help="get square root")
parser.add_argument("-p", "--edit", "--edd", action = "store_true", help = " new запись") 
               
args = parser.parse_args()
print(args)



if args.sqrt:
    answer = args.square**2
    mod = 'square'
    mod2 = f"{args.square}^2 = {answer}"
    
    
else:
    answer = math.sqrt(args.square)
    mod = 'square root'
    mod2 = f"\nsqrt({args.square}) = {answer}"
    

if args.verbosity == 2:
	if args.edit:
		f = open('text_sq.txt', 'a', encoding='utf-8')
		f.write(f"\nthe {mod} of {args.square} equals {answer}")
		f.close
		f.flush		
    
	#print(f"\nthe {mod} of {args.square} equals {answer}")
elif args.verbosity == 1:
	if args.edit:
		f = open('text_sq.txt', 'a', encoding='utf-8')
		f.write(f"\nthe {mod2}")
		f.close
		f.flush
else:
    print(answer)
