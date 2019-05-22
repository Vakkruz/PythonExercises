# Small file to experiment with command-line argument parsing.
# Used to know how to do it with Java but I wanna know how it works in Python

import argparse

# Copy pasted from official Python docs
parser = argparse.ArgumentParser(description='Process some integers.') #Sets up description for what program does

parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

args = parser.parse_args() #Useful for actually catching the args and (I assume) puts them into a list
print(args.integers)

#""".accumulate(args.integers))"""
