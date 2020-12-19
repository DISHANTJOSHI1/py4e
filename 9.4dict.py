"""Write a program to read through the mbox-short.txt and figure out who has sent
the greatest number of mail messages. The program looks for 'From ' lines and
takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to
a count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer."""




#fname = input('Enter file name: ')
fh = open('mbox-short.txt')
count = dict()

for line in fh:
    if line.startswith('From '):
        ln_splt = line.split()
        indx = ln_splt[1]
        #print(indx)
        count[indx] = count.get(indx,0)+1 #since email is not sequence in a list we don't use for loop
#print(count)
max_value = None #number of times max email are sent by a person
max_value_key = None #email of person
for name,cnt in count.items():
    if great is None or cnt>great: #we could have used #if cnt>max_value:
        max_value_key = name                                #max_value = cnt
        max_value_key = cnt                                 #max_value_key = name
print(max_value_key , max_value)
