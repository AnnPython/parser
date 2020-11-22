import argparse
import math

parser = argparse.ArgumentParser(usage = 'первый аргумент, второй аргумент', 
								description = "Производит действие над двумя аргументами",
								epilog = 'Всего хорошего и спасибо за рыбу')

parser.add_argument('A', type = float, help = 'Первое слагаемое')
parser.add_argument('B', type = float, help = 'Второе слагаемое')

parser.add_argument('-m', '--multiply', '--mul', action = "store_true", help = 'умножение')
parser.add_argument('-d', '--division', '--div', action = "store_true", help = 'деление')
parser.add_argument('-s', '--subtraction', '--sub', action = "store_true", help = 'вычитание')
parser.add_argument('-a', '--addiction', '--add', action = "store_true", help = 'сложение')
parser.add_argument('-o', '--writ', '--wrt', action = "store_true", help = 'запись')
parser.add_argument('-p', '--edit', '--edd', action = "store_true", help = ' new запись')
args = parser.parse_args()


if args.multiply:
	ans = args.A * args.B
	if args.writ:
			f = open('text.txt', 'w', encoding='utf-8')
			f.write(f'{ans}')
			f.close
			f.flush 
	elif args.edit:
			f = open('text.txt', 'a', encoding='utf-8')
			f.write(f'\nРезультат умножения ' +str(ans))
			f.close
			f.flush
	else:
		print(ans)
	
elif args.division:
	if args.B == 0:
		raise ValueError('На ноль делить нельзя!')
	ans = args.A / args.B
	if args.writ:            
	    f = open('text.txt', 'w', encoding='utf-8')
	    f.write(f'{ans}')
	    f.close
	    f.flush
	elif args.edit:
		f = open('text.txt', 'a', encoding='utf-8')
		f.write(f'\nРезультат деления ' +str(ans))
		f.close
		f.flush
	         
	else:
		print(ans)
elif args.subtraction:
	ans = args.A - args.B
	if args.writ:
		f = open('text.txt', 'w', encoding='utf-8')
		f.write(f'{ans}')
		f.close
		f.flush
	elif args.edit:
			f = open('text.txt', 'a', encoding='utf-8')
			f.write(f'\nРезультат вычитания ' +str(ans))
			f.close
			f.flush	 
	else:
		print(ans)
elif args.addiction:
	ans = args.A + args.B
	if args.writ:
		f = open('text.txt', 'w', encoding='utf-8')
		f.write(f'{ans}')
		f.close
		f.flush
	elif args.edit:
			f = open('text.txt', 'a', encoding='utf-8')
			f.write(f'\nРезультат сложения ' +str(ans))
			f.close
			f.flush	 
else:
    ans = args.A + args.B

    print(ans)
