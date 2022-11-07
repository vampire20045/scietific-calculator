import math 
print("Welcome to the calculator ")
print(" press + for addition")
print("press - for subtraction")
print("press * for multiplication")
print("press / for division")
print("enter sqrt for square root")
print("enter expo for power")
print("enter trigno for trignometric function")
print("enter conversions for conversions")
print("enter pow for power")
n=input("enter your choice")
if n=="+":
    a=eval(input("enter first number"))
    b=eval(input("enter second number"))
    print( "addition=",a+b)
elif n=="-":
    a=eval(input("enter first number"))
    b=eval(input("enter second number"))
    print("subtraction=",a-b)
elif n=="*":
    a=eval(input("enter first number"))
    b=eval(input("enter second number"))

    print("multiplication=",a*b)
elif n=="/":
    a=eval(input("enter first number"))
    b=eval(input("enter second number"))
    print("division=",a/b)
elif n=="%":
    a=eval(input("enter first number"))
    b=eval(input("enter second number"))

    print("mod=",a%b)
elif n=="sqrt":
    a=eval(input("enter a number"))
    x= math.sqrt(a)
    print(x)
elif n=="expo":
    c=eval(input())
    y=math.exp(c)
    print("exponent=",y)
elif n=="pow":
    a=eval(input("enter first number"))
    b=eval(input("enter second number"))
    kk=math.pow(a,b)
    print("power",kk)
elif n=="trigno":
    print(" enter cos for cos function")
    print(" enter sin for sin functions")
    print(" enter tan for tan functions")
    print(" enter cot for cot function")
    print(" enter sec for sec function")
    print(" enter cosec for cosec function")
    m=eval(input("enter a number"))
    h=input("enter a choice")
    def trigno(m):
        if h=="cos":
            p=math.cos(m)
            print(p)
        elif h=="sin":
            l=math.sin(m)
            print(l)
        elif h=="tan":
            i=math.tan(m)
            print(i)
        elif h=="cot":
            j=math.cot(m)
            print(j)
        elif h=="cosec":
            t=math.cosec(m)
            print(t)
        elif h=="sec":
            q=math.sec(m)
            print(q)
    trigno(m)
elif n=="conversions":
    print(" enter degree for conversion of radians to degree")
    print("enter radians for conversion of degrees to radians")
    l=eval(input("enter a number"))
    v=input()
    if v=="degree":
        s=math.degrees(l)
        print(s)
    elif v=="radians":
        g=math.radians(l)
        print(g)
else:
    print("enter valid and try again")
print("THANK YOU")    
        
        
        

