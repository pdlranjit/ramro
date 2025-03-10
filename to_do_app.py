#Simple GUI command ine task 
# TO run file in python we have to use {python filename.py}
add=[]
remove=[]
clas=[]
attempt=2
while True and attempt>=0:
    name=input('Do u want to add, remove, or numbered task in this list:').strip().lower()
    if name== 'add':
        mag=str(input('What u want to add:'))
        add.append(mag)
        print(f'u have enter  {mag} in the add task')
        attempt=attempt-1
        print(f'u have {attempt} attempt left in this game')
        
    elif name=='remove':
        mag=input('What u want to add in the remove section:')
        if mag in add:
            add.remove(mag)
            print(f'U have remove {mag} from the task:')
            
        else:
            print(f'We have add {mag} in the task')
        attempt=attempt-1
        print(f'u have {attempt} attempt left in this game')
        print('U have also enter in the remove task')
    elif name=='clas':
        mag=int(input('which  value u want to enter in this class :'))
        clas.append(mag)
        print(f'u have class {mag} in  the task')
        attempt=attempt-1
        print('u have {attempt} attempt left in this game')
        break
    else:
        attempt=attempt-1
        print(f'u have {attempt} attempt left in the list')
        print('u have enter the wrong command  try to be enter the right command ,please')
        
if attempt==0:
    print('u have  exit the program ,now u can do whatever u want to this program ')
else:
    print('u are trying to do some projects')
        