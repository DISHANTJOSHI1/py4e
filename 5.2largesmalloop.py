"""Write a program that repeatedly prompts a user for integer numbers until the
user enters 'done'. Once 'done' is entered, print out the largest and smallest
of the numbers. If the user enters anything other than a valid number catch it
 with a try/except and put out an appropriate message and ignore the number."""


smallest = None
largest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        a =float(num)
    except:
        print('invalid input')
        continue
    if smallest is None :
        smallest = a
    elif a<smallest:
        smallest  = a
    if largest is None:
        largest = a
    elif  a > largest:
        largest = a
print('Largest is: ',largest)
print('Smallest is: ',smallest)
