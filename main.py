# Imports
import tkinter as tk


# Functions for ASCII to Unicode and Unicode to ASCII conversions
def ascii_to_unicode(string):  # ascii to unicode
    if not string.isascii():  # if input string is not ascii
        raise ValueError("Input must be an ASCII character.")
    unicode_list = []  # define an empty list
    for char in string:  # iterating through characters in list
        # print(char, '\n')
        # print(ord(char), '\n')
        # print(hex(ord(char)), '\n')
        unicode_list.append(hex(ord(char)))  # ord() function returns the Unicode code for each character, which gets converted to hexadecimal with the hex() function, and added to the empty list
    return unicode_list


def unicode_to_ascii(string):  # unicode to ascii
    string1 = ""  # define an empty string
    for i in range(0, len(string), 2):  # iterates through every second character in string
        # print("hereE")
        # print(string[i:i + 2])
        # print("here1", '\n')
        hex1 = int(string[i:i + 2], 16)  # takes every second character and the character after it, converting them to hexadecimal and placing them withing the hex1 variable
        # print("here2", hex1, '\n')
        if hex1 < 0 or hex1 > 0x10FFFF:
            raise ValueError("Input must be a valid Unicode code point.")
        try:
            # print("here3", hex1, '\n')
            char1 = chr(int(hex1))  # converts hex1 to its decimal equivalent and passes it through chr() to return the string representing the decimal code
            # print(char1, '\n')
            string1 += char1  # concatenates each character from char1 into the empty string
            # return chr(string)
        except ValueError:
            raise ValueError(f"Invalid Unicode code point: {string}")
    return string1

# Function to handle conversion based on user input
def convert():
    conv_choice = conversion_choice.get()
    try:
        if conv_choice == 1:  # convert ASCII to unicode
            user_input = ascii_input.get()
            unicode_value = ascii_to_unicode(user_input)
            result_label.config(text=f"Result: Unicode value of {user_input} = {unicode_value}")
        elif conv_choice == 2:  # convert unicode to ASCII
            ascii_char = unicode_to_ascii(unicode_input.get())
            result_label.config(text=f"Result: ASCII character of {unicode_input.get()} = {ascii_char}")
    except ValueError as e:
        result_label.config(text=f"Error: {e}")


# Create main window
root = tk.Tk()
root.title("ASCII to Unicode and vice-versa Converter")


explanation_label = tk.Label(root, text="\nASCII and Unicode are both encoding systems but while\n"
                                        "Unicode uses a variable-length encoding scheme and can\n"
                                        "represent up to 1,114,112 characters, ASCII is encoded into\n"
                                        "7 bits and stored as 8-bit characters and hence, can only\n"
                                        "represent 128 characters, 256 if extended ASCII is included.\n"
                                        "However, ASCII is considered a subset of Unicode since the\n"
                                        "first 128 Unicode characters and their codes (in both decimal\n"
                                        "and hexadecimal form) are identical to ASCII.                       \n\n"
                                        "Note: ASCII decimal codes 0-31 (in hex: 0x00-0x1F) & 128-159\n"
                                        " (0x80-0x9F) are control characters and are non-printable\n")
explanation_label.grid(row=0, column=0)

# Create label and entry for ASCII input
ascii_label = tk.Label(root, text="ASCII input (e.g. Hello):")
# ascii_label.grid(row=2, column=0)
ascii_label.grid(row=1, column=0)
ascii_input = tk.Entry(root)
# ascii_input.grid(row=2, column=1)
ascii_input.grid(row=2, column=0)

# Create label and entry for Unicode input
unicode_label = tk.Label(root, text="\nUnicode input in hex (e.g. 48656C6C6F for Hello):")
# unicode_label.grid(row=3, column=0)
unicode_label.grid(row=3, column=0)
unicode_input = tk.Entry(root)
# unicode_input.grid(row=3, column=1)
unicode_input.grid(row=4, column=0)

blank_label1 = tk.Label(root, text="")
blank_label1.grid(row=5, column=0)
blank_label2 = tk.Label(root, text="")
blank_label2.grid(row=8, column=0)
blank_label3 = tk.Label(root, text="")
blank_label3.grid(row=10, column=0)
blank_label4 = tk.Label(root, text="")
blank_label4.grid(row=12, column=0)

# Create radio buttons for conversion choice
conversion_choice = tk.IntVar()
ascii_to_unicode_radio = tk.Radiobutton(root, text="ASCII to Unicode", variable=conversion_choice, value=1)
# ascii_to_unicode_radio.grid(row=4, column=0)
ascii_to_unicode_radio.grid(row=6, column=0)
# unicode_to_ascii_radio = tk.Radiobutton(root, text="Unicode to ASCII", variable=conversion_choice, value=2)
unicode_to_ascii_radio = tk.Radiobutton(root, text="Unicode to ASCII", variable=conversion_choice, value=2)
#unicode_to_ascii_radio.grid(row=4, column=1)
unicode_to_ascii_radio.grid(row=7, column=0)

# Create button to initiate conversion
convert_button = tk.Button(root, text="Convert", command=convert)
# convert_button.grid(row=5, column=0, columnspan=2)
convert_button.grid(row=9, column=0)

# Create label for conversion result
result_label = tk.Label(root, text="")
result_label.grid(row=11, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
