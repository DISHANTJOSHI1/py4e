#Calculateing avg using list
'''numlist = []
while True:
    a = input('Enter a number: ')
    if a == 'done':
        break
    try:
        inp = int(a)
    except :
        print('Invalid Input....')
        break
    numlist.append(inp)
avg = sum(numlist)/len(numlist)
print('The average is: ',avg)'''


# get all the mail IDs from mbox-short.txt where line startswith From. Also ount those lines

'''count = 0
a = open('mbox-short.txt','r')
for line in a:
    if line.startswith('From'):
        count = count+1
        word = line.split()
        print(word[1])
print('total count is: ',count)'''

# read romeo.txt file. Split each line and if words repeat then append it in the new list.
'''lst = []
file = open('romeo.txt')
for line in file:
    spl = line.split()
    for words in spl:
        if words not in lst:
            lst.append(words)
lst.sort()
print(lst)'''



      
        
