"""Write code using find() and string slicing (see section 6.10) to extract
the number at the end of the line below.
Convert the extracted value to a floating point number and print it out."""

text = "X-DSPAM-Confidence:    0.8475"
a = text.find(" ")
b = (text[a : 30])
#c = b.strip() // this would remove all spaces in a string
c = float(b) #since we r converting string to float we don't need strip() fn.
print(c)
