# ASCIIUnicodeConvert

## PSEUDOCODE

Import the tkinter module to create the GUI window

Define two functions:  
ascii_to_unicode(string) to convert ASCII characters to their Unicode equivalents  
&nbsp;&nbsp;&nbsp;&nbsp;Check if the input string is ASCII, raise an error if it is not  
&nbsp;&nbsp;&nbsp;&nbsp;Create an empty list  
&nbsp;&nbsp;&nbsp;&nbsp;Iterate through each character in the input string  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Use the ord() function to get the Unicode code for each character  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convert the Unicode code to hexadecimal using the hex() function and append it to the list  
&nbsp;&nbsp;&nbsp;&nbsp;Return the list 

unicode_to_ascii(string) to convert Unicode characters to their ASCII equivalents  
&nbsp;&nbsp;&nbsp;&nbsp;Create an empty string  
&nbsp;&nbsp;&nbsp;&nbsp;Iterate through every second character in the input string  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Take the iterated character and the character after it and define them as hexadecimal using the int() function  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[i.e. if the passed string was "4845", "48" & "45" would be taken and defined as hexadecimal]   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Convert the hexadecimal value to decimal using the int() function and then convert to a character using the chr() function  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[since the chr() function converts using the decimal codes of characters]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Append the character to the string  
&nbsp;&nbsp;&nbsp;&nbsp;Return the string

Define a function called convert() to handle the conversion based on user input  
&nbsp;&nbsp;&nbsp;&nbsp;Get the user's choice of conversion (ASCII to Unicode or Unicode to ASCII)  
&nbsp;&nbsp;&nbsp;&nbsp;If the choice is 1 (ASCII to Unicode), get the ASCII input from the user and pass it through the ascii_to_unicode() function  
&nbsp;&nbsp;&nbsp;&nbsp;If the choice is 2 (Unicode to ASCII), get the Unicode input from the user and pass it through the unicode_to_ascii() function  
&nbsp;&nbsp;&nbsp;&nbsp;Display the conversion result in a label  

Create the main window using tkinter  
Define a label to explain the program's purpose  
Create a label and entry for the ASCII input  
Create a label and entry for the Unicode input  
Create radio buttons to allow the user to choose the conversion type  
Create a button to initiate the conversion  
Create a label to display the conversion result  

Start the GUI event loop using root.mainloop()
