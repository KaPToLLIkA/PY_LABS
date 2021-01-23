from math import *


def C(args):
    return pi * args[0] * args[0]

def T(args):
    return (args[0] + args[1]) / 2 * args[2]

def R(args):
    return args[0] * args[1]


def calculate_v1(fns, args):
    def calculator(arg):
        try:
            f = fns[len(arg) - 1]
        except IndexError:
            return "index out of bounds, can't find function. args: " + str(arg) 

        try:
            return f(arg)
        except ValueError:
            return "wrong value. args: " + str(arg)
        except TypeError:
            return "wrong type. args: " + str(arg) 

    return map(calculator, args)

fns = [C, R, T]
args = [[1, 1], [1], [2, 3, 4], [3], [2, 4], ["ss", "ss"], [4, 4, 4, 4]]

print(*calculate_v1(fns, args), sep = '\n')