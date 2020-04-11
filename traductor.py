# -*- coding: utf-8 -*-

WORDS = {
        'hola': 'Hello ',
        'mi': 'my ',
        'nombre': 'name ',
        'es': 'is ',
        'yo': 'yo ',
        'y ': 'and ',
        'estoy': 'am ',
        'desarrollo': 'developing ',
        'en': 'in ',
        'que': 'What ',
        'donde': 'where ',
        'como': 'how ',
        'old': 'viejo ',
        'live': 'Vive ',
        'love': 'Hello ',
        'carro': 'car ',
        'trabajo': 'job',

}

def traductorEnglish(message):
    words = message.split(' ')
    trabslatedSentence = []
    translated_word = ''

    for word in words:
        try: 
            translated_word  += WORDS[str.casefold(word)]
            trabslatedSentence.append(translated_word)
        except KeyError:
            print('ohh, la palabra {0} no esta en el directorio'.format(word))


    return ' '.join(trabslatedSentence)


def traductorSpanish(mensaje):
    palabras = mensaje.split(' ')
    oracionTraducida = []

    for palabra in palabras:
        palabra_traducida = ''

        for key, value in WORDS.items():
            if  str.casefold(palabra) == value.rstrip():
                palabra_traducida += key

        oracionTraducida.append(palabra_traducida)
    


    return ' '.join(oracionTraducida)


def run():

    menssage = str(input('Escriba la palabra a traducir '))

    try: 
        opcion  =  int(input(''' Ingrese: 
                1: Ingles
                2: Español    
        '''))
    except NameError:
        print('oh, oh, Opcion no valida')
    except:
        print('No se')


    if (opcion == 1):
       traductor =  traductorEnglish(menssage)
    elif(opcion == 2):
        traductor =  traductorSpanish(menssage)
    else:
        print('oh, oh, Opcion no valida')

    print(traductor)



if __name__ == '__main__':
    run()