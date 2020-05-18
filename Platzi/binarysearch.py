# -*- coding: utf-8 -*-
import random 

def binary_search(numbers, number_to_find, low, high):
    
    numbers_sorted = sorted(numbers)
    if low > high:
        return False

    mid = int((low + high) / 2)

    if numbers_sorted[mid] == number_to_find:
        return True
    elif int(numbers_sorted[mid]) > number_to_find:
        return binary_search(numbers_sorted, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers_sorted, number_to_find, mid + 1, high)



def generate_list():
    lista = range(0,100)
    return random.sample(lista,k=10)


if __name__ == '__main__':
    numbers = generate_list()

    number_to_find = input('¿Que numero desea buscar:?')

    try:
        number = int(number_to_find)
        result = binary_search(numbers, number, 0, len(numbers) - 1)

        if result == True:
            print('Adivinaste')
        else:
            print('Fallaste')   

        print(numbers)   
    except ValueError:
        print('La entrada es incorrecta: escribe un numero entero')




    