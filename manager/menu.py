import os

def nav():
    while True:

        os.system('cls')

        print('==================')
        print('GESTOR DE CLIENTES')
        print('==================')
        print('')

        print('[1] Listar clientes\n[2] Mostrar Clientes\n[3] Añadir cliente\n[4] Modificar cliente\n[5] Borrar cliente\n[6] Salir')

        option = input('>')
        
        os.system('cls')

        if option == '1':
            print('Listado de clientes')
            # TODO
        elif option == '2':
            print('Mostrando cliente')
            # TODO
        elif option == '3':
            print('Añadiendo cliente')
            # TODO
        elif option == '4':
            print('Modificando cliente')
            # TODO
        elif option == '5':
            print('Borrando cliente')
            # TODO
        elif option == '6':
            print('Saliendo...')
            break
    
        input('Presione una ENTER para continuar...')
        
        



        

        

