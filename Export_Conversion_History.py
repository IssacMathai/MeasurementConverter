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

        # Disable Centimetres and Inches button while window is open
        partner.cm_and_in_welcome_screen_button.config(state=DISABLED)

        # Centimetres and Inches Converter child window
        self.cm_and_in_box = Toplevel()

        # Re-enables Centimetres and Inches button if the centimetres and inches converter window is closed using the X button
        self.cm_and_in_box.protocol('WM_DELETE_WINDOW', partial(self.close_Centimetres_and_Inches_Converter, partner))

        # GUI Frame
        self.cm_and_in_frame = Frame(self.cm_and_in_box, bg=background)
        self.cm_and_in_frame.grid()

        # Centimetres and Inches Converter heading (row 0)
        self.cm_and_in_heading = Label(self.cm_and_in_frame, text="Centimetres and Inches Converter",
                                 font="arial 18 bold", bg=background, padx=10, pady=10)
        self.cm_and_in_heading.grid(row=0)

        # conversion_history Button (row 1)
        self.conversion_history_button = Button(self.cm_and_in_frame, text="Conversion History", font=("Arial 14 bold"), command=self.Conversion_History, padx=10, pady=10)
        self.conversion_history_button.grid(row=1)

    def close_Centimetres_and_Inches_Converter(self, partner):
        # Re-enable Centimetres and Inches button in Welcome Screen
        partner.cm_and_in_welcome_screen_button.config(state=NORMAL)
        self.cm_and_in_box.destroy()

    def Conversion_History(self):
        get_Conversion_History = Conversion_History(self)

class Conversion_History:
    def __init__(self, partner):
        
        # Formatting variables
        ch_background = "#f060f7"

        # Disable Centimetres and Inches button while window is open
        partner.conversion_history_button.config(state=DISABLED)

        # Conversion History child window
        self.conversion_history_box = Toplevel()

        # Re-enables Conversion History button if the conversion history window is closed using the X button
        self.conversion_history_box.protocol('WM_DELETE_WINDOW', partial(self.close_Conversion_History, partner))

        # GUI Frame
        self.conversion_history_frame = Frame(self.conversion_history_box, bg=ch_background)
        self.conversion_history_frame.grid()

        # Heading (row 0)
        self.conversion_history_heading = Label(self.conversion_history_frame, text="Conversion History", font="arial 18 bold", bg=ch_background, padx=10, pady=10)
        self.conversion_history_heading.grid(row=0)

        # Export button (row 1)
        self.export_button = Button(self.conversion_history_frame, text="Export", font="Arial 14 bold", command=self.Export, padx=10, pady=10)
        self.export_button.grid(row=1)
    
    def close_Conversion_History(self, partner):
        #  Restore Conversion History button in centimetres and inches converter
        partner.conversion_history_button.config(state=NORMAL)
        self.conversion_history_box.destroy()
    
    def Export(self):
        get_export = Export(self)

class Export:
    def __init__(self, partner):

        # Formatting variables
        export_background = "#f060f7"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Export child window
        self.export_box = Toplevel()

        # Re-enables export button if the export window is closed using the X button
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # GUI Frame
        self.export_frame = Frame(self.export_box, bg=export_background)
        self.export_frame.grid()

        # Heading (row 0)
        self.export_heading = Label(self.export_frame, text="Export Conversion History", font="Arial 18 bold", bg=export_background)
        self.export_heading.grid(row=0)

        # Warning text (row 1)
        self.export_warning_text = Label(self.export_frame, text = "Please note that if the filename you enter below already exists, "
                                                                   "it will be replaced with your conversion history", justify=CENTER,
                                                                   bg="pink",fg="maroon", font = "Arial 10 italic", wrap=300,
                                                                   padx=10, pady=10)
        self.export_warning_text.grid(row=1, pady=10)

        # Input box (row 2)
        self.filename_input_box = Entry(self.export_frame, width=20, font="arial 12 bold")
        self.filename_input_box.grid(row=2, pady=10)

        # Save and cancel buttons frame
        self.save_cancel_buttons_frame = Frame(self.export_frame)
        self.save_cancel_buttons_frame.grid(row=3, pady=10)

        # Save button (row 3)
        self.save_button = Button(self.save_cancel_buttons_frame, text="Save", font="Arial 10 bold")
        self.save_button.grid(row=3)

        # Cancel button (row 3)
        self.cancel_button = Button(self.save_cancel_buttons_frame, text="Cancel", font="Arial 10 bold")
        self.cancel_button.grid(row=3, column=2)

        
    def close_export(self, partner):
        # Re-enable export button in Conversion History 
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy() 








# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()   