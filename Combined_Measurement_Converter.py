from tkinter import *
from functools import partial 
import random, re


class Welcome_Screen:
    def __init__(self, parent):
        # Formatting variables
        background_colour = "light blue"
        cm_and_in_button_colour = "lime green"
        m_and_ft_button_colour = "orange"

        # Frame
        self.welcome_screen_frame = Frame(width=200, height=200, bg=background_colour, pady=10)
        self.welcome_screen_frame.grid()

        # Main Heading (row 0)
        self.measurement_welcome_screen_label = Label(self.welcome_screen_frame, text = "Measurement Converter", font=("Arial", "20", "bold"), bg=background_colour, padx=10, pady=10)
        self.measurement_welcome_screen_label.grid(row=0)

        # Welcome Screen Buttons Frame
        self.welcome_screen_buttons_frame = Frame(self.welcome_screen_frame)
        self.welcome_screen_buttons_frame.grid(row=1, pady=10)

        # Centimetres and Inches Button (row 1)
        self.cm_and_in_welcome_screen_button = Button(self.welcome_screen_buttons_frame, text="Centimetres and Inches", bg=cm_and_in_button_colour, command=self.Centimetres_and_Inches_Converter, padx=10, pady=10)
        self.cm_and_in_welcome_screen_button.grid(row=1, column=0)

        # Metres and Feet Button (row 1)
        self.m_and_ft_welcome_screen_button = Button(self.welcome_screen_buttons_frame, text="Metres and Inches", bg=m_and_ft_button_colour, padx=10, pady=10)
        self.m_and_ft_welcome_screen_button.grid(row=1,column=1)
    
    def Centimetres_and_Inches_Converter(self):
        get_Centimetres_and_Inches_Converter = Centimetres_and_Inches_Converter(self)

class Centimetres_and_Inches_Converter:
    def __init__(self, partner):
        
        # Formatting variables
        background = "lime green"
        to_cm_button_background = "yellow"
        to_in_button_background = "tomato"

        # Create conversion history list
        self.conversion_history_list = []

        # disable Centimetres and Inches button when window is opened
        partner.cm_and_in_welcome_screen_button.config(state=DISABLED)

        # Centimetres and Inches Converter child window
        self.cm_and_in_box = Toplevel()
        
        # If users press cross at top, closes window and re-enables Centimetres and Inches button
        self.cm_and_in_box.protocol('WM_DELETE_WINDOW', partial(self.close_Centimetres_and_Inches_Converter, partner))

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
        self.to_convert__cm_in_input = Entry(self.cm_and_in_frame, width=20, font="Arial 20 bold")
        self.to_convert__cm_in_input.grid(row=2)

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
        self.cm_and_in_result_subheading_label = Label(self.cm_and_in_frame, font="Arial 14", bg=background, pady=10, text="Conversion Result:")
        self.cm_and_in_result_subheading_label.grid(row=4)

        # Conversion Result (row 5)
        self.cm_and_in_result_label = Label(self.cm_and_in_frame, font = "Arial 11 bold", bg=background, fg="blue", pady=10, text="")
        self.cm_and_in_result_label.grid(row=5)

        # Conversion History, Help and Dismiss buttons frame (row 6)
        self.cm_and_in_history_help_dismiss_buttons_frame = Frame(self.cm_and_in_frame)
        self.cm_and_in_history_help_dismiss_buttons_frame.grid(row=6, pady=10)

        # Conversion History button (row 6)
        self.cm_and_in_history_button = Button(self.cm_and_in_history_help_dismiss_buttons_frame, text="Conversion History", font="Arial 10 bold", bg="grey", padx=10, pady=10)
        self.cm_and_in_history_button.grid(row=6,column=0)

        # Help button (row 6)
        self.cm_and_in_help_button = Button(self.cm_and_in_history_help_dismiss_buttons_frame, text="Help", font="Arial 10 bold", bg="grey", padx=10, pady=10)
        self.cm_and_in_help_button.grid(row=6,column=1)

        # Dismiss button (row 6)
        self.cm_and_in_dismiss_button = Button(self.cm_and_in_history_help_dismiss_buttons_frame,
                                                                                                 text="Dismiss", font="Arial 10 bold", 
                                                                                                 bg="grey", 
                                                                                                 command=partial(self.close_Centimetres_and_Inches_Converter, partner),
                                                                                                 padx=10, pady=10)
        self.cm_and_in_dismiss_button.grid(row=6,column=2)

    def close_Centimetres_and_Inches_Converter(self, partner):
        # Put "Centimetres and Inches" button in welcome screen back to normal... 
        partner.cm_and_in_welcome_screen_button.config(state=NORMAL)
        self.cm_and_in_box.destroy()
    
    def cm_in_convert(self, inapplicable):

        to_convert_cm_in = self.to_convert_cm_in_input.get()

        try:
            to_convert_cm_in = float(to_convert_cm_in)
            cm_in_errors = "no"


            # Convert to centimetres if input is greater than 0
            if inapplicable == 0 and to_convert_cm_in > inapplicable:
                cm = (to_convert_cm_in * 2.54)
                to_convert_cm_in = self.rounding(to_convert_cm_in)
                cm = self.rounding(cm)
                answer = "{} in is {} cm".format(to_convert_cm_in, cm)

            # Convert to inches if input is greater than 0
            elif inapplicable == 0 and to_convert_cm_in > inapplicable:
                inches = (to_convert_cm_in * 2.54)
                to_convert_cm_in = self.rounding(to_convert_cm_in)
                inches = self.rounding(inches)
                answer = "{} cm is {} in".format(to_convert_cm_in, inches)

            else:
                # Input is unsuitable due to being negative or 0
                answer = "Please enter a positive number"
                cm_in_errors="yes"
            
            if cm_in_errors == "no":
                self.cm_and_in_result_label.configure(text=answer, fg="blue")
                self.to_convert__cm_in_input.configure(bg="white")

            else:
                self.cm_and_in_result_label.configure(text=answer, fg="pink")
                self.to_convert__cm_in_input.configure(bg="pink")
            
        except:
            print()


    
    def rounding(self, to_round):

        # If there is no remainder, print to 0dp
            if to_round %1 == 0:
                rounded = int(to_round)
        # Else, print to 2dp
            else:
                rounded = round(to_round, 2)
            return rounded


        




# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()                                 