from PIL import ImageColor
from tkinter import *
from tkinter import ttk
import pyperclip

print(ImageColor.getrgb("#000080"))

# Create an instance of Tkinter frame
win = Tk()

# Set the geometry of Tkinter frame
win.geometry("750x250")
win.title("Hex To RGB converter")


def display_text():
    global entry
    color = entry.get()

    # printing the hex color
    print("Hex Color: " + color)

    # displays confirmation of copied text
    confirmCopy.configure(text="Copied to clipboard!")

    # in case a user forgets to insert the #
    if color[0] != "#":
        # code below converts from hex to rgb
        rgbColor = ImageColor.getrgb("#" + color)

        # will display the converted color
        label.configure(text=rgbColor)

        # copying to clipboard
        pyperclip.copy(str(rgbColor))

    elif len(color) > 7:
        # in case a entered color exceeds the maximum color length
        label.configure(text="Please Insert a valid Hex color.")
    # default condition
    else:
        # code below converts from hex to rgb
        rgbColor = ImageColor.getrgb(color)

        # will display the converted color
        label.configure(text=rgbColor)

        # copying to clipboard
        pyperclip.copy(str(rgbColor))


# Initialize a Label to display the User Input
label = Label(win, text="", font=("Courier 22 bold"))
label.pack()

confirmCopy = Label(win, text="", font=("Courier 22 bold"))
confirmCopy.pack()

# Create an Entry widget to accept User Input
entry = Entry(win, width=40)
entry.focus_set()
entry.pack()

# Create a Button to validate Entry Widget
ttk.Button(win, text="Convert", width=20, command=display_text).pack(pady=20)

win.mainloop()
