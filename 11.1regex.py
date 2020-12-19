"""In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers."""



import re
sum = 0
count = 0
fl = open('regex_sum_243799.txt')
for line in fl:
    num=re.findall('([0-9]+)',line)
    for number in num:
        flt_num = float(number)
        count = count + 1
        sum = sum+flt_num
        print(flt_num)
print('SUM: ',sum ,'  & ''COUNT: ',count)
