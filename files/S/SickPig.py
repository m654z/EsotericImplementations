import random
import sys

words = ['GRUNT',
         'MOAN',
         'OINK',
         'BURP',
         'GROAN',
         'WHINE',
]

f = open(sys.argv[1], 'r')
code = f.read()
f.close()

if "PIG" in code:
    code = code.split("PIG")
    f = open(code[0], 'rw')
    f.write(random.choice(words))
    f.close()

else:
    raise PigError(random.choice(words))
