# this program displays an empty windows

import tkinter


class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # enter the tkinter main loop
        tkinter.mainloop()

    # create an instance of the myGUI class
my_gui = MyGUI()  # had an error, had to correct the indentation here