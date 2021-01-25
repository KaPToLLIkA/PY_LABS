from tkinter import *


class SimpleConstTableView(Frame):

    def __build_table__(self, parent, list_2d: list):
        self.rows = len(list_2d)
        self.columns = len(list_2d[0])


        self._widgets = []

        for row in range(self.rows):
            current_row = []
            for column in range(self.columns):
                item = Entry(self, borderwidth=0, width=10)

                item.insert(END, str(list_2d[row][column]))

                item.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                current_row.append(item)
            self._widgets.append(current_row)

        for column in range(self.columns):
            self.grid_columnconfigure(column, weight=1)

    def __init__(self, parent, list_2d):
        Frame.__init__(self, parent, background="black")
        self.__build_table__(parent, list_2d)

