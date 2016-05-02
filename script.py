#!/usr/bin/env python3

from argparse import ArgumentParser

from lib import multiply, divide, add, subtract


def main():
	parser = ArgumentParser()
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument("-a", "--add", nargs=2, type=int)
	group.add_argument("-d", "--divide", nargs=2, type=int)
	group.add_argument("-m", "--multiply", nargs=2, type=int)
	group.add_argument("-s", "--subtract", nargs=2, type=int)
	args = parser.parse_args()

	if args.add:
		print("Adding %s and %s" %tuple(args.add))
		print(add(*args.add))
	
	if args.subtract:
		print("Subtracting %s and %s" %tuple(args.subtract))
		print(subtract(*args.subtract))
	
	if args.multiply:
		print("Multiplying %s and %s" %tuple(args.multiply))
		print(multiply(*args.multiply))
	
	if args.divide:
		print("Dividing %s and %s" %tuple(args.divide))
		print(divide(*args.divide))


if __name__ == "__main__":
	main()
