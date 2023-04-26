from menu import Menu
from ClassEmail import Email
import os

if __name__ == '__main__':
    auxEmail = Email()
    xmenu = Menu()
    op = xmenu.mostrarMenu()
    while (op != 0):
        if (op >= 4):
            os.system('cls')
            print('ERROR, opcion elegida incorrecta. \nVuelva a intentar.')
            os.system('pause')
            op = xmenu.mostrarMenu()
        xmenu.manejadorMenu(op, auxEmail)
        op = xmenu.mostrarMenu()
    else: 
        print ('saliendo...')
        os.system('pause')
        os.system('exit')