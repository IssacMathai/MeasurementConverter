from tkinter import *
from functools import partial 
import random

class Welcome_Screen:
    def __init__(self, partner):
        
        # Formatting variables
        background_color = "light blue"
        
        # Welcome Screen GUI
        self.welcome_screen_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.welcome_screen_frame.grid()

        # Main Heading (row 0)
        self.measurement_welcome_screen_label = Label(self.welcome_screen_frame, text="Measurement Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.measurement_welcome_screen_label.grid(row=0)

        # Centimetres and Inches Button (row 1)
        self.cm_and_in_welcome_screen_button = Button(self.welcome_screen_frame, text="Centimetres and Inches", font=("Arial", "14"), command=self.Centimetres_and_Inches_Converter, padx=10, pady=10)
        self.cm_and_in_welcome_screen_button.grid(row=1)

    def Centimetres_and_Inches_Converter(self):
        get_Centimetres_and_Inches_Converter = Centimetres_and_Inches_Converter(self)

class Centimetres_and_Inches_Converter:
    def __init__(self, partner):
        
        # Formatting variables
        background = "lime green"
        to_cm_button_background = "yellow"
        to_in_button_background = "tomato"

        # disable Centimetres and Inches button while window is open
        partner.cm_and_in_welcome_screen_button.config(state=DISABLED)

        # Centimetres and Inches Converter child window
        self.cm_and_in_box = Toplevel()
        
        # If users press cross at top, closes window and re-enables Centimetres and Inches button


        # GUI Frame
        self.cm_and_in_frame = Frame(self.cm_and_in_box, bg=background)
        self.cm_and_in_frame.grid()

        # Centimetres and Inches Converter heading (row 0)
        self.cm_and_in_heading = Label(self.cm_and_in_frame, text="Centimetres and Inches Converter",
                                 font="arial 18 bold", bg=background, padx=10, pady=10)
        self.cm_and_in_heading.grid(row=0)

        # User instructions (row 1)
        self.cm_and_in_instructions_label = Label(self.cm_and_in_frame, text="Type in a measurement below and push the button you wish to convert the measurement to.",
                                        font="Arial 10 italic", wrap=300,
                                         justify=CENTER, bg=background,
                                        padx=10, pady=10)
        self.cm_and_in_instructions_label.grid(row=1)

        # Measurement input box (row 2)
        self.to_convert_input = Entry(self.cm_and_in_frame, width=20, font="Arial 20 bold")
        self.to_convert_input.grid(row=2)

        # "To Convert" buttons frame
        self.to_cm_and_in_buttons_frame = Frame(self.cm_and_in_frame)
        self.to_cm_and_in_buttons_frame.grid(row=3, pady=10)

        # To Centimetres button (row 3)
        self.to_cm_button = Button(self.to_cm_and_in_buttons_frame, text="To Centimetres", font="Arial 10 bold", bg=to_cm_button_background, padx=10, pady=10)
        self.to_cm_button.grid(row=3, column=0)

        # To Inches button (row 3)
        self.to_in_button = Button(self.to_cm_and_in_buttons_frame, text="To Inches", font="Arial 10 bold", bg=to_in_button_background, padx=10, pady=10)
        self.to_in_button.grid(row=3,column=1)

        # Conversion Result subheading (row 4)
        self.cm_and_in_result_subheading_label = Label(self.cm_and_in_frame, font="Arial 14", bg=background, padx=10, pady=10, text="Conversion Result:")
        self.cm_and_in_result_subheading_label.grid(row=4)





# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()

