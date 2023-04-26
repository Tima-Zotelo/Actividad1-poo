class Email:
    __idCuenta = str
    __dom = str
    __tipoDom = str
    __contr = str
    def __init__ (self, idcuenta=None, dominio=None, tipoDominio=None, contraseña=None):
        self.__idCuenta = idcuenta
        self.__dom = dominio
        self.__tipoDom = tipoDominio
        self.__contr = contraseña
    
    def retornaEmail(self):
        return (self.__idCuenta + '@' + self.__dom + '.' + self.__tipoDom)
    
    def getTipoDominio(self):
        return (self.__tipoDom)

    def crearCuenta (self, correo, contraseña):
        if (correo.find('@')):
            aux_correo = correo.split('@')
            cuenta = aux_correo [0]
            if (correo.find('.')):
                aux_correo2 = correo.split('.')
                dom = aux_correo2[0]
                tdom = aux_correo2[1]
                self.__init__(cuenta, dom, tdom, contraseña)
                print ('Correo creado con exito!')
            else: print ('Error, el dominio no tiene punto "." ')
        else: print ('Error, el correo no tiene @')

    def modificarContr (self):
        aux = input('Ingrese su contraseña actual: ')
        if aux != self.__contr:
            print ('Error, contraseña incorrecta. Vuelva a intentar')
            self.modificarContraseña()
        else:
            xCont = input('Ingrese su nueva contraseña: ')
            self.__contr = xCont
            print ('Contraseña cambiada con exito!\n')
        return