"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Tommi Poikolainen
050093232
tommi.poikolainen@tuni.fi
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__bmi = 0
        self.__result = StringVar()
        self.__bmitext = "BMI: 0.00"
        self.__result.set(self.__bmitext)

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow,
                                         text="Calculate",
                                         command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow,
                                   textvariable=self.__result)

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow,
                                        text="")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow,
                                    text="Stop",
                                    command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_value.grid(row=0, column=0)
        self.__height_value.grid(row=0, column=1)
        self.__calculate_button.grid(row=1, column=0)
        self.__stop_button.grid(row=1, column=1)
        self.__result_text.grid(row=2, column=0, columnspan=2, sticky=E + W)
        self.__explanation_text.grid(row=3, column=0, columnspan=2,
                                     sticky=E + W)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """
        try:
            weight = int(self.__weight_value.get())
            height = int(self.__height_value.get()) / 100

            if weight < 0 or height < 0:
                self.__explanation_text.configure(text="Error: height and "
                                                       "weight must be "
                                                       "positive.")
                self.reset_fields()
                return

            self.__bmi = weight / height ** 2
            round(self.__bmi, 2)
            self.__bmitext = "BMI: %.2f" % self.__bmi
            self.__result.set(self.__bmitext)

            if self.__bmi < 18.5:
                self.__explanation_text.configure(text="You are underweight.")
            elif self.__bmi > 25:
                self.__explanation_text.configure(text="You are overweight.")
            else:
                self.__explanation_text.configure(
                    text="Your weight is normal.")

        except:
            self.__explanation_text.configure(text="Error: height and weight "
                                                   "must be numbers.")
            self.reset_fields()
            return

    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__bmi = 0
        self.__bmitext = "BMI: %.2f" % self.__bmi
        self.__result.set(self.__bmitext)

        self.__weight_value.delete(0, 'end')
        self.__height_value.delete(0, 'end')

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
