
# String slicing and parsing # Task is to extract the number in text as float
'''text = 'X-DSPAM-Confidence:   0.8475'
pos = text.find("0")
a = float(text[22:])
print(a)
print(type(a))'''

# To count number of lines in a file
'''count = 0
file = open('mbox.txt')
for line in file:
    count = count+1
print(count)'''

#To extract all lines that has '@uct.ac.za' in them
"""fhandle = open('mbox.txt')
for line in fhandle:
    line = line.rstrip()
    if '@uct.ac.za' in line:
        print(line)"""

# try and except
'''a = input('Enter a file name:  ')
count = 0
try:
    file = open(a)
except:
    print('File name is not valid...')
    quit()
for line in file:
    count = count+1
print(count)'''

# Assignment ___Read the file and print it in capital letter
'''file = open('words.txt')
for line in file:
    line = line.rstrip().upper()
    print(line)'''


# Find the line ''X-DSPAM-Confidence' & extract float values in them and find avg of all those values
'''file = open('mbox.txt')
count = 0
sum = 0
for line in file:
    line = line.rstrip()
    if 'X-DSPAM-Confidence' in line:
        count = count+1
        pos = line.find(' ')
        #print(line, '\n', pos)
        fl_val=float(line[pos:])
        sum = sum+fl_val

print('\n''Total Count is: ',count)
print('Sum is: ',sum)
print('Thus average of all floating values from line is: ',sum/count)'''
