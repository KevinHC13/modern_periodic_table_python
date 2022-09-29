import os


class tabla:
    def __init__(self,op):
        self.op = op
    pass
    
    def menu_exp(self):
        first=False
        util = utilities()
        util.banner()
        print("Enter the corresponding no")
        print("1.Serch by 'NAME'")
        print("2.Serch by 'SYMBOL'")
        print("3.Serch by 'ATOMIC NUMBER'")
        print("4.Serch by 'ATOMIC WRIGHT'")
        op = util.inputs_Select()
        if op==0:
            op = self.menu_exp()
        return op    

    def explore(self):
        util = utilities()
        op = self.menu_exp()
        if(op>=1 and op<=4):

            if(op==1):
                InputData=input("Enter the name: ")
            elif(op==2):
                InputData=input("Enter the symbol: ")
            elif(op==3):
                InputData=input("Enter the atomic number: ")
            elif(op==4):
                InputData=input("Enter the atomic weight: ")

            arElements=util.separate_items()

            for i in range(0,len(arElements)):
                if arElements[i][op] == InputData:
                    util.banner()
                    if arElements[i][1]!="":
                        print("Name:"+str(arElements[i][1]))
                    else:
                        print("Name: Empty")
                    if arElements[i][2]!="":
                        print("Symbol:"+str(arElements[i][2]))
                    else:
                        print("Symbol: Empty")
                    if arElements[i][3]!="":
                        print("Atomic No:"+str(arElements[i][3]))
                    else:
                        print("Atimic No: Empty")
                    if arElements[i][4]!="":
                        print("Atomic Wt:"+str(arElements[i][4]))
                    else:
                        print("Atomic Wt: Empty")
                    if arElements[i][5] != "":
                        print("Comment:"+str(arElements[i][5]))
                    else:
                        print("Comment: Empty")
                    return
            util.banner()
            print("Data not found")
        else:
            print("Invalid option")
            exit

    def add(self):
        util = utilities()
        util.banner()
        name=input("Name: ")
        symbol=input("Symbol: ") 
        number=input("Atomic Number: ")
        weight=input("Atomic weight: ") 
        comments= input("Comment: ")
        if util.data_exist(name,symbol,number,weight) != True:    
            data = open("POO/data.txt","a")
            data.write(util.read_last_item()+","+name+","+symbol+","+number+","+weight+","+comments+"\n")
            data.close    
            print("Data saved")
        else:
                print("Data exist")


class utilities:
    def __init__(self):
        pass

    def pause(self):
        input("Press enter to continue...")

    def banner(self):
        os.system("clear")
        print("Modern Periodic Table")
        print("Digital")
        print("________\n")

    def inputs_Select(self):
        inputOp=input(":") or "0"
        if not(inputOp =="1" or  inputOp=="2" or inputOp=="3" or inputOp=="4"):
            inputOp="0"
        return int(inputOp) 

    def menu(self):
        self.banner()    
        print("Enter the corresponding no")
        print("1.Add new Element Information")
        print("2.Explore")
        print("3.Quit")
        return self.inputs_Select()

    def separate_items(self):
        data = open("POO/data.txt","r")
        arData = data.readlines()
        arElements=[]
        for i in range(0,len(arData)):
            arElements.append(arData[i].split(','))
        return arElements
    
    def data_exist(self,name,symbol,number,weight):
        arElements=self.separate_items()
        flag_exists=False
        for i in range(0,len(arElements)):
            for j in range(1,4):
                if j == 1:
                    if name!="":
                        if arElements[i][j]==name:
                            flag_exists=True
                elif(j==2):
                    if symbol!="":
                        if arElements[i][j]==symbol:
                            flag_exists=True
                elif(j==3):
                    if number!="":
                        if arElements[i][j]==number:
                            flag_exists=True
                elif(j==4):
                    if weight!="":
                        if arElements[i][j]==weight:
                            flag_exists=True
        return flag_exists

    def read_last_item(self):
        data = open("POO/data.txt","r")
        arData = data.readlines()
        data.close
        return str(len(arData))

class Main():
    def main():
        data=open("POO/data.txt","a+")
        data.close
        first=False
        table = tabla(first)
        util = utilities()
        op=util.menu()

        while(op!=3 or first==False):
            first=True
            if(op==1):
                table.add()
                util.pause()
            elif(op==2):
                table.explore()
                util.pause()
            elif(op==3):
                print("Exiting...")
                break
            else:
                print("Invalid option")
                util.pause()
            if(first==True):
                op=util.menu()


Main.main()