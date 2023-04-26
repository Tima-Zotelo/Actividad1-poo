from ClassEmail import Email
import os
import csv

class Menu:
    __op: int

    def __init__(self):
        self.__op = None
    
    def mostrarMenu (self):
        os.system('cls')
        print ('------->Menu principal')
        print ('1. Crear usuario nuevo (inciso 1)\n2. Modificar contraseña (inciso 2)\n3. Leer un archivo (inciso 4) \n4. mostrar Dominio \n0. Salir')
        op = int (input('seleccione opcion: '))
        return op

    def manejadorMenu (self, op, auxCorreo):
        if op == 1:
            self.opcion1(auxCorreo)
        elif op == 2:
            self.opcion2(auxCorreo)
        elif op == 3:
            self.opcion3(auxCorreo)

    def opcion1(self, auxCorreo):
        os.system('cls')
        print ('Procederemos a crear su correo:')
        nombre = input ('Ingrese su nombre: ')
        correo = input ('ingrese su correo: ')
        contr = input ('ingrese su contraseña: ')
        auxCorreo.crearCuenta(correo, contr)
        print (f'Estimado {nombre}, te enviaremos tus mensajes a la direccion {correo}')
        os.system("pause")
        os.system("cls")

    def opcion2 (self, auxCorreo):
        os.system('cls')
        auxCorreo.modificarContr()
        os.system('pause')

    def opcion3 (self,auxCorreo):
        correos = []
        cont = 0
        path = './Correos.csv'
        archivo = open(path, "r")
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            idCuenta = fila[0]
            dominio = fila[1]
            tDominio = fila[2]
            contr = fila[3]
            Nuevo_Correo = Email(idCuenta, dominio, tDominio, contr)
            correos.append(Nuevo_Correo)
        print ('fin For, Carga Lista')
        os.system('pause')
        os.system('cls')
        xDom = input ('ingrese dominio que se desea buscar: ')
        for i in correos:
            if i.getTipoDominio() == xDom:
                cont +=1
            
        print (f'La cantidad de correos con el dominio "{xDom}" es: {cont}')
        os.system('pause')
    
