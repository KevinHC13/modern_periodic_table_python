"""
Materia: Programacion orientada a objetos
Profesor: Dr. Marco Aurelio Nuño Maganda
Alumno: Kevin Alejandro Hernandez Campillo

Tabla periodica moderna
En el proyecto se realizo una tabla periodica que nos permite añadir nuevos elementos a un registro y examinar los 
elementos ya existentes.
"""

import os


class tabla:
    def __init__(self,op):
        self.op = op
    pass
    
    """
    Muestra el submenu de la seccion explorar y permite seleccionar una de las opciones.
    Entradas: Ninguna entrada
    Salidas: Retorna un entero que es la seleccion del usuario
    """
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
    """
    Este método realiza la funcion de explorar, donde la opcion seleccionada por el usuario es tomada para pedir al usuario
    que ingrese el parametro de busqueda, posteriormente se compara este parametro con los argumentos de cada elemento, si 
    se encuentra una coincidencia entonces se imprime la informacion del elemento, de lo contrario se indica que el elemento
    no existe.
    Entrada: Ninguna entrada
    Salida: Sin salidas
    """
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

    """
    Funcion para añadir elementos nuevos. Se pide al usuario que ingrese los datos del elemento, posteriormente se valida si
    estos datos existen ya en el archivo, de no ser asi entonces se guardan el registro como una nueva linea en el fichero,
    de lo contrario no se guarda.
    Entrada: Ninguna entrada
    Salida: Ninguna salida
    """
    def add(self):
        util = utilities()
        util.banner()
        name=input("Name: ")
        symbol=input("Symbol: ") 
        number=input("Atomic Number: ")
        weight=input("Atomic weight: ") 
        comments= input("Comment: ")
        if util.data_exist(name,symbol,number,weight) != True:    
            data = open("data.txt","a")
            data.write(util.read_last_item()+","+name+","+symbol+","+number+","+weight+","+comments+"\n")
            data.close    
            print("Data saved")
        else:
                print("Data exist")


class utilities:
    def __init__(self):
        pass

    """
    Funcion simple que se encarga de pausar el programa mientras el usuario no ingrese un enter.
    Entrada: Ninguna entrada
    Salida: Ninguna salida
    """
    def pause(self):
        input("Press enter to continue...")

    """
    Limpia la terminal e imprime un baner sobre alguna infomracion del programa
    Entrada: Ninguna entrada
    Salida: Ninguna salida
    """
    def banner(self):
        os.system("clear")
        print("Modern Periodic Table")
        print("Digital")
        print("________\n")

    """
    Valida si el usuario ingreso una opcion posible, de lo contrario pide al usuario que seleccione una opcion otra vez.
    Entrada: Ninguna entrada
    Salida: Se retorna la opcion elegida del usuario
    """
    def inputs_Select(self):
        inputOp=input(":") or "0"
        if not(inputOp =="1" or  inputOp=="2" or inputOp=="3" or inputOp=="4"):
            inputOp="0"
        return int(inputOp) 


    """
    Imprime el menu principal del programa y nos permite seleccionar una con el metodo anterior.
    Entrada: Ninguna entrada
    Salida: Retorna la opcion elegida por el usuario
    """
    def menu(self):
        self.banner()    
        print("Enter the corresponding no")
        print("1.Add new Element Information")
        print("2.Explore")
        print("3.Quit")
        return self.inputs_Select()

    """
    Este metodo separa cada uno de los elementos de un String separandolos por coma.
    Entrada: Ninguna entrada.
    Salida: Retorna una lista que contiene sublistas con los atribitos separados.
    """
    def separate_items(self):
        data = open("data.txt","r")
        arData = data.readlines()
        arElements=[]
        for i in range(0,len(arData)):
            arElements.append(arData[i].split(','))
        return arElements
    
    """
    Este metodo verifica si un dato que se quiere ingresar ya esta registrado, comparando cada atributo con todos los 
    elementos registrados.
    Entrada: nombre, simbolo, numero y peso atomico
    Salida: Un valor booleano, si no se encuentran elementos repetidos se retorna False, de lo contrario se retorna True.
    """
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
    
    """
    Lee el ultimo elemento que existe en el registro para poder llevar un conteo en el indice de los renglones.
    Entrada: Ninguna entrada
    Salida: Retorna un string con la informacion del ultimo elemento. 
    """
    def read_last_item(self):
        data = open("data.txt","r")
        arData = data.readlines()
        data.close
        return str(len(arData))

class Main():
    def main():
        data=open("data.txt","a+")
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