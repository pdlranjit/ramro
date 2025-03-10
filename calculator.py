def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x *y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return 'this is not possible'


print('Enter the operation u want to be perfomed:')
print('1.ADD')
print('2.SUBTRACT')
print('3.MULTIPLY')
print('4.DIVISON')
    
user=input('Which option u will chose(1,2,3,4):: ')
num1=int(input('enter the first number: '))
num2=int(input('enter the second number: '))
if user in ['1','2','3','4']:
    if user=='1':
        result=num1+num2
        print(f'Output of {num1}+{num2} is::: {result}' )
    elif user=='2':
        result=num1-num2
        print(f'output of{num1}-{num2} is :: {result}')
    elif user=='3':
        result=multiply(num1,num2)
        print(f'output of {num1} * {num2} is :: {result}')
    elif user=='4':
        result = divide(num1, num2)
        print(f'Output of {num1} / {num2} is:: {result}')
    else:
        print("Invalid input! Please choose a valid option.")


    
