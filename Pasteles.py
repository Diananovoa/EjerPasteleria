import sys
import numpy as np

class RegistroVenta:
    arreglo = []
    def __init__(self, nombre=None, costo=None, tamano=None, aptoDiabeticos=None):
        self.nombre = nombre
        self.costo = costo
        self.tamano = tamano
        self.aptoDiabeticos = aptoDiabeticos
        
    def agregar(self):
        self.nombre = input('Ingrese por favor el nombre del pastel : ')
        self.costo = input('Digite el valor que tiene el pastel : ')
        self.tamano = input('Que tamaño tiene el pastel o para cuantas personas es : ')
        self.aptoDiabeticos = input('Es apto para diabeticos : si - no ? : ')
        var = [self.nombre,self.costo,self.tamano,self.aptoDiabeticos]
        self.arreglo.append(var)
    def mostrar(self):
        for row in self.arreglo:
            print(f'El tipo de este pastel es : {row[0]} ,tiene un costo o valor de : {row[1]},en porciones es para {row[2]} personas y {row[3]} es apto para diabetico ')

            
    def buscar(self):
        self.nombre = input('\nIngrese el nombre de un producto a buscar: ')
        for row in self.arreglo:
            if row[0] == self.nombre:
                print('\n---- Este producto si existe ----')
                print(f'El tipo de este pastel es : {row[0]} ,tiene un costo o valor de : {row[1]},en porciones es para {row[2]} personas y {row[3]} es apto para diabetico ')
            elif row[0] != self.nombre:
                print("Nos permitimos informar que no existe el producto que esta buscando")

obj = RegistroVenta()
while (True):
    print('\n')
    print('-'*5, 'Menu de opciones para nuestra pateleria', '-'*5)
    print('digite -1 Para ingresar un pastel')
    print('digite -2 Para listar la compra')
    print('digite -3 Para buscar por nombre')
    print('digite -4 Para salir del programa')
    print('*'*25)
    print(' '*10)
    opcion = int(input('Digite una opcion por favor:  '))
    if opcion == 1:
        obj.agregar()
    elif opcion == 2:
        obj.mostrar()
    elif opcion == 3:
        obj.buscar()
    elif opcion == 4:
        print('Gracias por su compra, Felices festividades')
        sys.exit(0)
    else:
        print('Opcion invalida')