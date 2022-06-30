# -*- coding: utf-8 -*-
from tkinter import Tk, Button, Entry, END


class main:
    def __init__(self):
        self.window = window
        self.window.title('ip calculate')
        self.window.minsize(width=300, height=200)
        self.entry = Entry(width=60, bg="white", fg="black")
        self.entry.pack()
        self.entry.insert(0, "Введите ip")
        self.button = Button(self.window,
                             text="Перевести ip в 2 СС",
                             width=20,
                             height=2,
                             bg="white",
                             fg="black",
                             command=self.ip_to_binary)
        self.button.pack()
        self.button = Button(self.window,
                             text="Перевести ip в 10 СС",
                             width=20,
                             height=2,
                             bg="white",
                             fg="black",
                             command=self.ip_back)
        self.button.pack()
        self.window.mainloop()

    def ip_to_binary(self):
        ip_test = self.entry.get()
        ip_config = []
        ip_test = ip_test.split(".")
        if len(ip_test) != 4:
            return

        def ip_convert(ip):
            i = 0
            act = 7
            binary = ''

            while i < 8:
                if ip >= 2**act:
                    binary += '1'
                    ip = ip - 2**act
                else:
                    binary += '0'
                i += 1
                act -= 1
            ip_config.append(binary)

        for x in ip_test:
            ip_convert(int(x))
        self.entry.delete(0, END)
        self.entry.insert(0, '.'.join(ip_config))

    def ip_back(self):
        binary = self.entry.get()
        ip_decod = []
        binary = binary.split(".")
        if len(binary) != 4:
            return

        def ip_convert(ipb):
            i = 0
            act = 7
            encodip = 0
            while i < 8:
                if ipb[i] == '1':
                    encodip = encodip + 2**act
                i += 1
                act -= 1
            ip_decod.append(encodip)

        for x in binary:
            ip_convert(list(x))
        self.entry.delete(0, END)
        self.entry.insert(0, '.'.join(str(e) for e in ip_decod))


window = Tk()

main()
