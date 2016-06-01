import sys

def parse(command):
    if command == "A programming language is a formal constructed language designed to communicate instructions to a machine, particularly a computer.":
        print("A programming language is a formal constructed language designed to communicate instructions to a machine, particularly a computer.")

with open(sys.argv[1], 'r') as f:
    code = f.read()

parse(code)
