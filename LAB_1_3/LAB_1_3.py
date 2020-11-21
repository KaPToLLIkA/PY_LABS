from math import *

def getFloat():
    while(True):
        try:
            return float(input("Print value: "));
        except ValueError:
            print("Not a number!");


def main():

    while(True):
        task = input("""
C - circle;
T - trapeze;
R - rectangle;
E - exit
Print: """);
        if task.startswith("C") or task.startswith("c"):

            print("Print r: ");
            r = getFloat();
            print("S: " + str(pi * r ** 2));

        elif task.startswith("T") or task.startswith("t"):

            print("Print a, b, h: ");
            a, b, h = getFloat(), getFloat(), getFloat();
            print("S: " + str((a + b) / 2.0 * h));

        elif task.startswith("R") or task.startswith("r"):

            print("Print a, b: ");
            a, b = getFloat(), getFloat();
            print("S: " + str(a * b));

        elif task.startswith("E") or task.startswith("e"):
            break;
        else:
            print("Wrong command!");


    return;


main();