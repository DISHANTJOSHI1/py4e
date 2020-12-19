"""Program to prompt user to enter input.Find sum and average of the NUMBERS
entered by user.Once user type 'done' execute the final result and instead of
'done' if user enter any other string give a proper error msg by using try/except
"""


num = 0
total = 0.0
while True:
    a = input("Enter the number: ")
    if a == 'done':
        break
    try:

        b = float(a)
    except:
        print('invalid input')
        continue
    total = total + b
    num = num + 1
print('SUM IS:',total, '\n'  'TOTAL NUMBERS ARE:',num, '\n' 'AVERAGE IS:',total/num)
