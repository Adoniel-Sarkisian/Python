
#__________________________________________________________________________________________________________________________________
        
def add():
    a=float(input('first number: '))
    b=float(input('second number: '))
    c=float(input('third number: '))
    if a==0:
        print(b+c)
    if b==0:
        print(a+c)
    if c==0:
        print(a+b)
    else:
        print(a+b+c)
  
def subtract():
    a=float(input('first number: '))
    b=float(input('second number: '))
    c=float(input('third number: '))
    if a==0:
        print(b-c)
    if b==0:
        print(a-c)
    if c==0:
        print(a-b)

def multiply():
    a=float(input('firt number: '))
    b=float(input('second number: '))
    c=float(input('third number: '))
    if a==0:
        print(b*c)
    if b==0:
        print(a*c)
    if c==0:
        print(a*b)
    else:
        print(a*b*c)
    
def devide():
    a=float(input('first number: '))
    b=float(input('second number: '))
    c=float(input('third number: '))
    if a==0:
        print(b/c)
    if b==0:
        print(a/c)
    if c==0:
        print(a/b)
    else:
        print(a/b/c)
        
#__________________________________________________________________________________________________________________________________
    
def quest():
    i=input('what do you want to do (add/subtract/multiply/devide)')

    if i=='add':
        add()

    if i=='subtract':
        subtract()

    if i=='multiply':
        multiply()

    if i=='devide':
        devide()

#__________________________________________________________________________________________________________________________________
    
def quest3():
    j=input('do you want to cuntinue(yes/no) ')

    if j=='yes':
        quest()

        quest3()
    else:
        print('alright bye bye')
        
#____________________________________________________________________________________________________________________________________

quest()

quest3()
