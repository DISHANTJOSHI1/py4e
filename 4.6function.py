"""Write a program to prompt the user for hours and rate per hour using input to
compute gross pay. Pay should be the normal rate for hours up to 40 and
time-and-a-half for the hourly rate for all hours worked above 40 hours.
Put the logic to do the computation of pay in a function called computepay()
and use the function to do the computation."""

def computepay(h,r):
    if (h>40):
        p = (n*1.5*r)+(40*r)
        print("You r a assiduous person")
    else:
        p = h*r
        print('You really need to work hard')

    return p

hrs = input("Enter Hours: ")
rate = input("Enter rate: ")
h=float(hrs)
r = float(rate)
n=h-40
p = computepay(h,r)
print(p)
