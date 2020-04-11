# -*- coding: utf-8 -*-
PRODUCT = {
    'AREQUIPO': 10000,
    'ARROZ': 2000,
    'PAN': 1000,
    'CEBOLLA': 500,
    'AJO': 100,
    'TOMATE': 1500,
    'PESCADO': 5190,
    'POLLO': 10000,
    'CARNE': 3500,
    'PAPA': 990,
}

RATES = {
    'EURO': 4185,
    'DOLAR': 3827,
    'BITCOIN': 26390306,
    'PESOS': 1,
}




def checkin (items, rate):
    gross_price = 0
    net_precio = 0
    IVA = 0 
    factura = dist()


    for item in items:
        gross_price += PRODUCT[item]/RATES[rate]


    IVA = gross_price*0.19
    net_precio = gross_price + IVA
    print(gross_price)
    print(net_precio)



def retes_sw(i):
        switcher={
                1:'EURO',
                2:'DOLAR',
                3:'BITCOIN',
                4:'PESOS'
             }
        return switcher.get(i, 'oups  la moneda no existe')

    


def run ():
        items = []
        while True:
            item = input('''
            Ingrese el nombre del prodcuto:

            para factura pulse f 


            
            ''');

            if item.lstrip().rstrip() == str.casefold('f'):
                break
            
            items.append(item)
        
        rate = input('''
            [1]: EUROS
            [2]: DOLAR
            [3]: BITCOIN
            [4]: PESOS
        
        ''')
        if rate.isnumeric():

            rete_str = retes_sw(int(rate))
            checkin(items,rete_str)
        else:
            print('ohh creo que no ingresaste un numero')


            

if __name__ == '__main__':
    run ()


