from math import *


def main():
    print("Print m, x, y, a: ")
    m, x, y, a = [float(i) for i in input().split(' ')]

    if (m < -1.0):
        print("m should be greater then -1.0");
        return;

    if (m * a > 100.0):
        print("m * a is too large");
        return;

    denominator = (1 + 2 * x) ** (a * m) - 1;

    if (denominator == 0.0):
        print("denominator equals zero");
        return;

    numerator = exp(sqrt(m + 1.0)) * abs(x - y);

    print("f(m, x, y, a) = " + str(numerator / denominator - (x + y) ** (m * a)));


main();
