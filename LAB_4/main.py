import re as re
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox as mb

from Doctor import *
from DataBase import *
from SimpleConstTableView import *

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


def comparator(d1: Doctor, d2: Doctor):
    return int(d1.work_experience) == int(d2.work_experience)


def get_fields_as_list(d: Doctor):
    return [d.tab_number, d.last_name, d.first_name, d.patronymic, d.speciality, d.work_experience, d.work_hours,
            d.office, d.phone]


def build_table_data(objects: list):
    table_2d = [Doctor.field_names]

    for item in objects:
        table_2d.append(get_fields_as_list(item))
    return table_2d


class App(Tk):
    def __remove_proc(self):
        error_msg = ""
        if not self.__remove_frame_childs['tab_number'].get():
            error_msg += "Empty field: tab_number\n"

        if error_msg:
            mb.showerror("Input error", error_msg)
            return

        if self.__db.remove_by_key(self.__remove_frame_childs['tab_number'].get()):
            self.__show_proc()
            mb.showinfo("Success", "Doctor removed")

    def __find_proc(self):
        error_msg = ""
        if not re.fullmatch(self.__rx_check_number, self.__find_frame_childs['work_experience'].get()):
            error_msg += "Wrong work experience (in hours), example: 60\n"

        if not self.__find_frame_childs['work_experience'].get():
            error_msg += "Empty field: work_experience\n"

        if error_msg:
            mb.showerror("Input error", error_msg)
            return

        result = self.__db.find_by_value(
            Doctor(work_experience=int(self.__find_frame_childs['work_experience'].get())),
            comparator
        )

        table_view = Toplevel(self)
        SimpleConstTableView(table_view, build_table_data(result)).pack(fill="both")
        mb.showinfo("Success", "Result size: {0} rows".format(len(result)))

    def __show_proc(self):
        table_view = Toplevel(self)
        SimpleConstTableView(table_view, build_table_data(self.__db.data_dict.values())).pack(fill="both")

    def __add_proc(self):
        error_msg = ""
        if not re.fullmatch(self.__rx_check_phone, self.__add_frame_childs['phone'].get()):
            error_msg += "Wrong phone, example: 81237891278 or +71237891278\n"

        if not re.fullmatch(self.__rx_check_date, self.__add_frame_childs['work_hours'].get()):
            error_msg += "Wrong work hours, example: 12:00-18:00\n"

        if not re.fullmatch(self.__rx_check_number, self.__add_frame_childs['work_experience'].get()):
            error_msg += "Wrong work experience (in hours), example: 60\n"

        if self.__check_empty_fields_flag.get():
            for field in Doctor.field_names:
                if not self.__add_frame_childs[field].get():
                    error_msg += "Empty field: " + field + "\n"

        if error_msg:
            mb.showerror("Input error", error_msg)
            return

        self.__db.add_by_key(
            self.__add_frame_childs['tab_number'].get(),
            Doctor(
               tab_number=self.__add_frame_childs['tab_number'].get(),
               last_name=self.__add_frame_childs['last_name'].get(),
               first_name=self.__add_frame_childs['first_name'].get(),
               patronymic=self.__add_frame_childs['patronymic'].get(),
               speciality=self.__add_frame_childs['speciality'].get(),
               work_experience=self.__add_frame_childs['work_experience'].get(),
               work_hours=self.__add_frame_childs['work_hours'].get(),
               office=self.__add_frame_childs['office'].get(),
               phone=self.__add_frame_childs['phone'].get()
            )
        )

        self.__show_proc()
        mb.showinfo("Success", "Doctor added")

    def __init__(self):
        Tk.__init__(self)

        self.__rx_check_date = "^(([0-1][0-9])|(2[0-3])):(([0-5][0-9])|(60))\\-(([0-1][0-9])|(2[0-3])):[0-5][0-9]$"
        self.__rx_check_phone = "^((\\+7)|8)\\d{10}$"
        self.__rx_check_number = "^[1-9]\\d*$"

        self.__db = DataBase()

        self.__tab_control = Notebook(self)

        self.__add_frame = Frame(self.__tab_control)
        self.__remove_frame = Frame(self.__tab_control)
        self.__find_frame = Frame(self.__tab_control)
        self.__show_info_frame = Frame(self.__tab_control)

        self.__tab_control.add(self.__add_frame, text="Add info")
        self.__tab_control.add(self.__remove_frame, text="Remove info")
        self.__tab_control.add(self.__find_frame, text="Find info")
        self.__tab_control.add(self.__show_info_frame, text="Show all info")

        self.__tab_control.pack(fill="both")

        self.__check_empty_fields_flag = BooleanVar()
        self.__check_empty_fields_flag.set(1)

        self.__add_frame_childs = {
            'tab_number': Entry(self.__add_frame),
            'last_name': Entry(self.__add_frame),
            'first_name': Entry(self.__add_frame),
            'patronymic': Entry(self.__add_frame),
            'speciality': Combobox(self.__add_frame, values=Doctor.specialities),
            'work_experience': Entry(self.__add_frame),
            'work_hours': Entry(self.__add_frame),
            'office': Entry(self.__add_frame),
            'phone': Entry(self.__add_frame),
            'add_button': Button(self.__add_frame, text="Add", command=self.__add_proc)
                .grid(row=len(Doctor.field_names) + 1, column=0, sticky="nsew", padx=1, pady=1),
            'check_empty_fields_flag': Checkbutton(self.__add_frame, text="Check empty fields?",
                                                   variable=self.__check_empty_fields_flag)
                .grid(row=len(Doctor.field_names), column=0, sticky="nsew", padx=1, pady=1)
        }

        for i in range(len(Doctor.field_names)):
            Label(self.__add_frame, text=Doctor.field_names[i])\
                .grid(row=i, column=0, sticky="nsew", padx=1, pady=1)
            self.__add_frame_childs[Doctor.field_names[i]]\
                .grid(row=i, column=1, sticky="nsew", padx=1, pady=1)

        self.__show_info_frame_childs = {
            'button': Button(self.__show_info_frame, text="Show", command=self.__show_proc).pack(side=LEFT),
        }

        self.__find_frame_childs = {
            'button': Button(self.__find_frame, text="Find", command=self.__find_proc).pack(side=LEFT),
            'work_experience': Entry(self.__find_frame),
        }

        Label(self.__find_frame, text="work_experience").pack(side=LEFT)
        self.__find_frame_childs['work_experience'].pack(side=LEFT)

        self.__remove_frame_childs = {
            'button': Button(self.__remove_frame, text="Remove", command=self.__remove_proc).pack(side=LEFT),
            'tab_number': Entry(self.__remove_frame),
        }

        Label(self.__remove_frame, text="tab_number").pack(side=LEFT)
        self.__remove_frame_childs['tab_number'].pack(side=LEFT)


if __name__ == "__main__":
    app = App()
    app.title("App")
    app.mainloop()
