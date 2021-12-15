"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""

from tkinter import *


class Counter:
    def __init__(self):
        self.__mainwindow = Tk()

        self.__number = 0
        self.__text = StringVar()
        self.__text.set(str(self.__number))

        self.__current_value_label = Label(self.__mainwindow,
                                           textvariable=self.__text)
        self.__current_value_label.grid(row=0,
                                        column=1,
                                        columnspan=2,
                                        sticky=E + W)

        self.__reset_button = Button(self.__mainwindow,
                                     text="Reset",
                                     command=self.reset)
        self.__reset_button.grid(row=1, column=0)

        self.__increase_button = Button(self.__mainwindow,
                                        text="Increase",
                                        command=self.increase)
        self.__increase_button.grid(row=1, column=1)

        self.__decrease_button = Button(self.__mainwindow,
                                        text="Decrease",
                                        command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)

        self.__quit_button = Button(self.__mainwindow,
                                    text="Quit",
                                    command=self.close)
        self.__quit_button.grid(row=1, column=3)

        self.__mainwindow.mainloop()

    def reset(self):
        self.__number = 0
        self.__text.set(self.__number)

    def increase(self):
        self.__number += 1
        self.__text.set(self.__number)

    def decrease(self):
        self.__number -= 1
        self.__text.set(self.__number)

    def close(self):
        self.__mainwindow.destroy()


def main():
    Counter()


if __name__ == "__main__":
    main()
