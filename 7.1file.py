""" Write a program that prompts for a file name, then opens that file and reads
through the file, and print the contents of the file in upper case. Use the file
words.txt to produce the output below."""

fh = open('words1.txt')
#fname = input("Enter file name: ") # words1.txt
#fh = open(fname)
#a = fh.read()
#b=a.upper()
#c= b.rstrip()
#print(c)
#OR OR OR OR OR
for line in fh:
    #line = line.upper()
    line = line.strip()
    print(line.upper())
