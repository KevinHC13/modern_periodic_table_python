import os

data=open("data.txt","a+")
data.close

def pause():
    input("Press enter to continue...")

def banner():
    os.system("clear")
    print("Modern Periodic Table")
    print("Digital")
    print("________\n")

def menu():
    banner()    
    print("Enter the corresponding no")
    print("1.Add new Element Information")
    print("2.Explore")
    print("3.Quit")
    return int(input(":") or 0)

def read_last_item():
    data = open("data.txt","r")
    arData = data.readlines()
    data.close
    return str(len(arData))

def add():
    banner()
    name=input("Name: ")
    symbol=input("Symbol: ")
    number=input("Atomic Number: ")
    weight=input("Atomic weight: ")
    comments= input("Comment: ")
    data = open("data.txt","a")
    data.write(read_last_item()+","+name+","+symbol+","+number+","+weight+","+comments+"\n")
    data.close    
    print("Data saved")

def menu_exp():
    first=False

    banner()
    print("Enter the corresponding no")
    print("1.Serch by 'NAME'")
    print("2.Serch by 'SYMBOL'")
    print("3.Serch by 'ATOMIC NUMBER'")
    print("4.Serch by 'ATOMIC WRIGHT'")
    op=int(input(":") or 0)
    if op==0:
        op = menu_exp()
    return op

def separate_items():
    data = open("data.txt","r")
    arData = data.readlines()
    arElements=[]
    for i in range(0,len(arData)):
        arElements.append(arData[i].split(','))
    return arElements

def explore():
    op=menu_exp()
    if(op>=1 and op<=4):
        
        if(op==1):
            InputData=input("Enter the name: ")
        elif(op==2):
            InputData=input("Enter the symbol: ")
        elif(op==3):
            InputData=input("Enter the atomic number: ")
        elif(op==4):
            InputData=input("Enter the atomic weight: ")
        
        arElements=separate_items()
        
        for i in range(0,len(arElements)):
            if arElements[i][op] == InputData:
                banner()
                print("Name:"+str(arElements[i][1]))
                print("Symbol:"+str(arElements[i][2]))
                print("Atomic No:"+str(arElements[i][3]))
                print("Atomic Wt:"+str(arElements[i][4]))
                print("Comment:"+str(arElements[i][5]))
                return
        banner()
        print("Data not found")
    else:
        print("Invalid option")
        #pause()
        exit

    
            
            
first=False
counter=0
op=menu()
while(op != 3 or first==False):
    first=True

    if(op==1):
        add()
        pause()
    elif(op==2):
        explore()
        
        pause()
    elif(op==3):
        print("Exiting...")
        break
    else:
        print("Invalid option")
        pause()
    if(first==True):
        op=menu()