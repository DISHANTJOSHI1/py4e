"""Write a program to read through the mbox-short.txt and figure out the
distribution by hour of the day for each of the messages. You can pull the hour
out from the 'From ' line by finding the time and then splitting the string a
second time using a colon.
"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
Once you have accumulated the counts for each hour, print out the counts,
sorted by hour as shown below."""


fh = open('mbox-short.txt')
count = dict()
lst = list()
for line in fh:
    if not line.startswith('From '):
        continue
    splt = line.split(" ")
    #print(splt)'
       #tm = line[31 : ]
    indx_time = splt[6]  #here to get time don't make mistake of using another for loop
    #print(indx_time) # to get any element from extracted line we don't use for loop instead use basic slicing techniques
    splt_time = indx_time.split(":") # see psedo code at the end
    #print(splt_time)
    indx_hr = splt_time[0]
    #print(indx_hr)
    count[indx_hr] = count.get(indx_hr,0)+1 #it will create a dictionary named count and store it as {'k',v} form
#print(count)
for k,v in count.items(): #since count is dictionary we can use 2 itr.variables and method items()
    new = (k,v)
    lst.append(new) # it will add key & value in list as a single tuple as [('k',v),('k',v),...]
    lst = sorted(lst) # it will sort list in ascending order for key and not value. For value check notes
#lst = sorted(lst,reverse.True) #it will sort list in descendin order depending on the key and not value
#print(lst)
for key,value in lst: # this for loop will break the list and give key value in a verical line
    print(key,value)




##here is some pseudocode to help
#split() on the spaces
#index time
#split() on the ':'
#index hours
