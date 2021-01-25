from Doctor import *
from DataBase import *

#Doctor(
#    tab_number = "", 
#    last_name = "", 
#    first_name = "", 
#    patronymic = "", 
#    speciality = "", 
#    work_experience = , 
#    work_hours = "", 
#    office = "", 
#    phone = "")


db = DataBase()


def comparator(d1: Doctor, d2: Doctor):
    int(d1.work_experience) == int(d2.work_experience)

def get_work_exp():
    while(True):
       try:
           return int(input("Work experience: "))
       except ValueError:
           print("Input error")

while(True):
    cmd = input("1 - Add\n2 - Remove\n3 - Print\n4 - Find\n0 - Exit\n")

    if (cmd[0] == "0"):
        break

    if (cmd[0] == "1"):
        tab_number = input("Tab number: ")

        db.add_by_key(tab_number,
                      Doctor(tab_number = tab_number, 
                            last_name = input("Last name: "), 
                            first_name = input("First name: "), 
                            patronymic = input("Patronymic: "), 
                            speciality = input("Speciality: "), 
                            work_experience = get_work_exp(), 
                            work_hours = input("Work hours: "), 
                            office = input("Office: "), 
                            phone = input("Phone: ")))

    if (cmd[0] == "2"):
        tab_number = input("Tab number: ")
        db.remove_by_key(tab_number)

    if (cmd[0] == "3"):
        db.print_all()

    if (cmd[0] == "4"):
        print(*db.find_by_value(Doctor(work_experience = get_work_exp()), comparator))