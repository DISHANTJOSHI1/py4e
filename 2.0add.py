a=input('enter a: ')
b=input('enter b: ')
d=float(a)
e=float(b)
if(d<=100 and d>= -100): #for 100<=D<= -100
    if(e<=100 and e>= -100): #for 100<=e<= -100
        c=d+e
        print("c: ",c)
else:
    print("error")
