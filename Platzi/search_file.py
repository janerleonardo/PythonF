
def run():
    counter = 0
    with open('numero.txt') as f:
        for line in f:
            counter += line.count('1')

    print('Numero 1 esta {0}'.format(counter))


if __name__=='__main__':
    run()