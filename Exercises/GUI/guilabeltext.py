__author__ = 'kadar'
import tkinter

class MyGUI:
    def __init__(self):
        # create the main window widget.
        self.main_window = tkinter.Tk()

        # create a label widget containing the text
        # text 'Hello World!'
        self.label = tkinter.Label(self.main_window, \
                                   text='Hello World!')

        # call the label widget's pack method
        self.label.pack()

        # enter the tkinter main loop
        tkinter.mainloop()

# create an instance of the MyGUI class
my_gui = MyGUI()