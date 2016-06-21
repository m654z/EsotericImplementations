import math
import sys

class Interpreter:
    stack = []
    bit32 = {'EAX': 0, 'EBX': 0, 'ECX': 0, 'EDX': 0}
    bit16 = {'AX': 0, 'BX': 0, 'CX': 0, 'DX': 0}
    bit8 = {'AH': 0, 'AL': 0, 'BH': 0, 'BL': 0,
            'CH': 0, 'CL': 0, 'DH': 0, 'DL': 0}

    def bits(self, n):
        return math.floor(math.log(n, 2)) + 1

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def print_reg(self, r):
        if r in self.bit8:
            print(self.bit8[r], end='')

        elif r in self.bit16:
            print(self.bit16[r], end='')

        elif r in self.bit32:
            print(self.bit32[r], end='')

        else:
            raise SyntaxError("Invalid register " + r + ".")

    def run(self, code):
        i = 0
        code = code.replace('\n', ' ').split(' ')

        while i < len(code):
            if code[i] == 'MOV':
                i += 1
                n = int(code[i])
                i += 1
                r = code[i]

                bits = self.bits(n)

                if bits <= 8 and r in self.bit8:
                    self.bit8[r] = n

                elif bits <= 16 and r in self.bit16:
                    self.bit16[r] = n

                elif bits <= 32 and r in self.bit32:
                    self.bit32[r] = n

                else:
                    raise MemoryError("Error: can't store " + str(bits) +
                                      " bit integer in " + r + ".")

            elif code[i] == 'PUSH':
                i += 1
                try:
                    self.push(int(code[i]))

                except TypeError:
                    self.push(code[i])

            elif code[i] == 'POP':
                i += 1
                r = code[i]

                val = self.pop()
                bits = self.bits(val)

                if bits <= 8 and r in self.bit8:
                    self.bit8[r] = val

                elif bits <= 16 and r in self.bit16:
                    self.bit16[r] = val

                elif bits <= 32 and r in self.bit32:
                    self.bit32[r] = val

                else:
                    raise MemoryError("Error: can't store " + str(bits) +
                                      " bit integer in " + r + ".")

            elif code[i] == 'CHR':
                i += 1
                r = code[i]

                if r in self.bit8:
                    self.bit8[r] = chr(self.bit8[r])

                elif r in self.bit16:
                    self.bit16[r] = chr(self.bit16[r])

                elif r in self.bit32:
                    self.bit32[r] = chr(self.bit32[r])

                else:
                    raise SyntaxError("Invalid register " + r + ".")

            elif code[i] == 'MSG':
                i += 1
                r = code[i]

                if r.startswith('[') and r.endswith(']'):
                    r = r[1:]
                    r = r[:-1]
                    r.split(', ')
                    for i in range(0, len(r)):
                        self.print_reg(r[i])

                else:
                    self.print_reg(r)

            elif code[i] == 'INC':
                i += 1
                r = code[i]

                if r in self.bit8:
                    self.bit8[r] += 1

                elif r in self.bit16:
                    self.bit16[r] += 1

                elif r in self.bit32:
                    self.bit32[r] += 1

                else:
                    raise SyntaxError("Invalid register " + r + ".")

            elif code[i] == 'DEC':
                i += 1
                r = code[i]

                if r in self.bit8:
                    self.bit8[r] -= 1

                elif r in self.bit16:
                    self.bit16[r] -= 1

                elif r in self.bit32:
                    self.bit32[r] -= 1

                else:
                    raise SyntaxError("Invalid register " + r + ".")

            elif code[i] == 'SQR':

                i += 1
                r = code[i]

                if r in self.bit8:
                    self.bit8[r] *= self.bit8[r]

                elif r in self.bit16:
                    self.bit16[r] *= self.bit16[r]

                elif r in self.bit32:
                    self.bit32[r] *= self.bit32[r]

                else:
                    raise SyntaxError("Invalid register " + r + ".")

            i += 1

i = Interpreter()
f = open(sys.argv[1], 'r')
i.run(f.read())
f.close()
