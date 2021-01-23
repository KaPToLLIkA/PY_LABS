from math import *




def fraction(m, x, y, a):
    def denominator(m, x, y, a):
        try:
            return (1 + 2 * x) ** (m * a) - 1
        except OverflowError:
            print("m or a are too large")
            return 1

    def numerator(m, x, y, a):
        return exp(sqrt(m + 1.0)) * abs(x - y)

    return numerator(m, x, y, a) / denominator(m, x, y, a)

def substraction(x1, x2, m, x, y, a):
    return x1(m, x, y, a) - x2(m, x, y, a)

def polynominal(m, x, y, a):
    try:
        return (x + y) ** (m * a);
    except OverflowError:
        print("m or a are too large")
        return 0

def function(m, x, y, a):
    return substraction(fraction, polynominal, m, x, y, a)

try:
    m, x, y, a = [float(i) for i in input("print m, x, y, a separated by spaces: ").split(' ')]
    print("f(m, x, y, a) = " + str(function(m, x, y, a)))
except ValueError:
    print("input error")



