from classEmail import Email 
from menu import Menu
import os

def test():
	print('''***** TEST ******
Datos correctos a probar:
correo.1@gmail.com, correo2@unsj.edu, matiaszotelo@yahoo.com

Datos incorrectos a probar:
correo3gmail.com, corre4@yahoo''')
	prueba = Email()
	print('\n\n---> DATOS CORRECTOS')
	print('correo.1@gmail.com')
	prueba.crearCuenta('correo.1@gmail.com','contra1')
	print('correo2@unsj.edu')
	prueba.crearCuenta('correo2@unsj.edu','contra2')
	print('matiaszotelo@outlook.com')
	prueba.crearCuenta('matiaszotelo@outlok.com','contra3')
	print('\n---> DATOS INCORRECTOS')
	print('correo3gmail.com')
	prueba.crearCuenta('correo3gmail.com','contra4')
	print('corre4@yahoo')
	prueba.crearCuenta('corre4@yahoo','contrasena5')
	os.system('Pause')
	os.system('cls')	

op = int(input ("""
Elija una opcion:
1. Ejecutar test
2. Ir al menu principal
"""))
if op == 1:
	test()
else:
	print('---> Menu Principal<---')
	op = int (input('''
			Seleccione una opcion:
			1. item 1
			2. item 2
			3. item 3
			4. item 3
			'''))
	nuevoMail = Email()
	xmenu = Menu()
	xmenu.opcionesMenu(op, nuevoMail)
#else: print ('opcion elegida incorrecta')