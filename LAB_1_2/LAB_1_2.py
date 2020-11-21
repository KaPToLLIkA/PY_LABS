import random;

list = [(int(i) if (random.randint(0, 1) == 0) else float(i)) for i in range(1, 20)];

def getInt():
    while(True):
        try:
            return int(input());
        except ValueError:
            print("Not a number!");
            


def getFloat():
    while(True):
        try:
            return float(input());
        except ValueError:
            print("Not a number!");

def t1():
    global list;
    print(list);
    return;


def t2():
    global list;
    
    print("Select type: 1-int, 2-float, 3-str");
    type = input();

    print("Print value:");
    if(type == "1"):
        list.append(getInt());
    elif(type == "2"):
        list.append(getFloat());
    elif(type == "3"):
        list.append(input());
    else:
        print("Wrong type!");

    print(list);
    return;

def t3():
    global list;
    print(list);
    print("Print element index (from 0): ");

    index = getInt();
    if (index < 0 or index >= len(list)):
        print("Index out of bounds");
    else:
        del list[index];

    return;


def t4():
    global list;
    
    cortage = tuple(value for value in list if (type(value) is float) and (value >= 0.0));

    print(list);
    print(cortage);

    return;


def t5():
    global list;

    result = 1;
    for value in list:
        if type(value) is int:
            result *= value;
    print(list);
    print(result);
    return;


def t6():
    global list;

    string = "";
    string = string.join([str(value) for value in list]);
    
    
    print(list);
    print(string);

    target = input("Print target str: ");

    result = string.find(target);
    count = 0;
    while(result != -1):
        count += 1;
        string = string[result+1:len(string)];
        result = string.find(target);
    
    print(count);
    return;


def t7():
    global list;
    set1 = set(list);
    print("Print 10 integers: ");
    set2 = {getInt() for i in range(0, 10)}

    print(set1);
    print(set2);
    print(set1.symmetric_difference(set2));
    return;


def t8():
    global list;
    dictionary = {list.index(value): value for value in list}

    print(dictionary);
    for item in dictionary.items():
        if item[0] % 2 != 0:
            print(item[1]);

    return;

def main():
    while(True):
        print(
"""1) show the list values on the screen;
2) adding new items to the end of the list (add items of different types);
3) deleting the user-specified item from the list;
4) form a tuple consisting of real positive elements of the list;
display the contents of the tuple on the screen;
5) find the product of all integer elements in the list;
6) generate a string from the values of the list items and count how many times
the user-specified word occurs in the string;
7) set the set M1 from the keyboard, form the set M2 from the list; output to
display the symmetric difference between sets M1 and M2;
8) get a dictionary from the list, use the key of each element to make the position of the element in the
dictionary; display the dictionary elements with odd key values line by line on the screen.
9) exit""");

        cmd = str(input());

        if (cmd == "1"):
            t1();
        elif(cmd == "2"):
            t2();
        elif(cmd == "3"):
            t3();
        elif(cmd == "4"):
            t4();
        elif(cmd == "5"):
            t5();
        elif(cmd == "6"):
            t6();
        elif(cmd == "7"):
            t7();
        elif(cmd == "8"):
            t8();
        elif(cmd == "9"):
            break;
        else:
            print("try again");
    print("end work");

main();

