from tkinter import *
from socket import *
from tkinter.messagebox import *
import re as re

window = Tk()
textin = Entry(window)
flag = IntVar()


def send(s: socket, data: str):
    end_seq = "#"
    data += end_seq
    s.send(data.encode("utf-8"))


def get(s: socket):
    res_str = ""
    end_seq = "#"
    while (True):
        tmp_dt = s.recv(2048)
        tmp_str = tmp_dt.decode("utf-8")
        res_str += tmp_str
        if res_str.endswith(end_seq):
            return res_str[0:len(res_str)-len(end_seq)]


def main():
    global window
    global textin
    global flag

    def send_proc():
        global window
        global textin
        global flag

        res_str = textin.get()
        error_msg = ""
        if flag.get() == 0:
            error_msg += "SET COMMAND TYPE! (ENCODE OR DECODE)\n"

        if not re.fullmatch("^[A-Z]*$", res_str):
            error_msg += "AVAILABLE ONLY A-Z CHARACTERS!\n"

        if error_msg:
            showerror("ERROR", error_msg)
            return

        client = socket()
        client.connect(('localhost', 25565))


        if flag.get() == 2:
            res_str += '-'
        if flag.get() == 1:
            res_str += '+'

        send(client, res_str)
        textin.delete(0, END)
        textin.insert(0, get(client))
        client.close()

    Button(window, text="send", command=send_proc).pack(side=LEFT)
    Label(window, text="message").pack(side=LEFT)

    textin.pack(side=LEFT)

    Radiobutton(window, text="Encode", value=1, variable=flag).pack(side=BOTTOM)
    Radiobutton(window, text="Decode", value=2, variable=flag).pack(side=BOTTOM)

    window.mainloop()


main()



