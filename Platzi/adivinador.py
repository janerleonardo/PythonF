# -*- coding: utf-8 -*-
import random

def main():
    ingresa_values()


def ingresa_values():
    number = random.randint(1000,10000)
    print('Tal vez el número que estás pensando es: {}'.format(number))
    print('')

    lista = list(str(number))
    lista_picas = ['F','F','F','F']
    lista_fallas = []
    #print(lista)

    num_no_encontrado = True

    while num_no_encontrado:
        respuesta = raw_input('Por favor, dame una pista P&F: ')

        i = 0
        for letra in respuesta:

            if letra.upper() == 'P':
                lista_picas[i] = lista[i]
            elif letra.upper() == 'F':
                lista_fallas.extend(lista[i])

            i += 1

        #print(str(''.join(lista_picas)))
        #print(lista_fallas)

        if 'F' in lista_picas:
            number = arma_nuevo_numero(lista_picas, lista_fallas) #random.randint(1000,10000)
            lista = list(str(number))
            lista_fallas = []
            print('')
            print('Oops, he fallado, tal vez el número es: {}'.format(number))
        else:
            print('He adivinado... tu numero es: {}'.format(''.join(lista_picas)))
            num_no_encontrado = False


    #unitPrice = float(raw_input('Precio unitario: '))
    #quantity = float(raw_input('Cantidad: '))

    #calc_neto(unitPrice,quantity)

def arma_nuevo_numero(lista_picas, lista_fallas):
    lista_picas_temp = lista_picas[:]

    lista_fallas_temp = lista_fallas[:]
    random.shuffle(lista_fallas_temp)
    for caracter in lista_fallas_temp:
        if 'F' in lista_picas_temp:
            lista_picas_temp[lista_picas_temp.index('F')] = caracter

    #Para los que su respuesta no es ni P ni F, o sea, para los que no están en el numero se completa un ramdomico
    while 'F' in lista_picas_temp:
        lista_picas_temp[lista_picas_temp.index('F')] = str(random.randint(0,9))

    print(lista_picas)
    return int(''.join(lista_picas_temp))


def calc_neto(unitPrice,quantity):

    netoValue = unitPrice * 1.19 * quantity

    print ('El valor neto del producto es: %f') % (netoValue)



if __name__ == '__main__':
    main()
