import pickle
import tkinter.filedialog as f
import tkinter.messagebox as m
from DataBase import *


class FileProcessor:
    def __init__(self, db: DataBase):
        self.db = db
        self.file_opened = False
        self.new_file = True
        self.cur_file = ""

    def save_proc(self):
        if self.file_opened:
            pickle.dump(self.db.data_dict, open(self.cur_file, "wb"))
            return

        if self.new_file:
            self.cur_file = f.asksaveasfilename()
            if self.cur_file:
                pickle.dump(self.db.data_dict, open(self.cur_file, "wb"))
            return

    def create_proc(self):
        self.file_opened = False
        self.new_file = True
        self.cur_file = ""
        self.db.data_dict = {}
        m.showinfo("New file", "New empty file created")

    def load_proc(self):
        self.cur_file = f.askopenfilename()
        if self.cur_file:
            self.file_opened = True
            self.new_file = False
            self.db.data_dict = pickle.load(open(self.cur_file, "rb"))


