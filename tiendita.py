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

def print_invoice(factura,gross_price,net_precio,IVA):
    print('''
        -------------------------------------------------------------
        ----------------- La Tiendita HAY OME------------------------
        Artiulo                             Precio
    
    ''')
    for key, value in factura.items():
        print('{0}                           {1}'.format(key,value))

    print('IVA                          {0}'.format(gross_price))
    print('Precio bruto                 {0} '.format(gross_price))
    print('Precio Neto                  {0}'.format(net_precio))




def checkin (items, rate):
    gross_price = 0
    net_precio = 0
    IVA = 0 
    factura = {}


    for key, value  in items.items():
        unit_price = (PRODUCT[key]*value)/RATES[rate]
        gross_price += unit_price
        factura[key] = unit_price


    IVA = gross_price*0.19
    net_precio = gross_price + IVA

    print(gross_price)
    print(net_precio)
    print(factura)
    print_invoice(factura,gross_price,net_precio,IVA)



def retes_sw(i):
        switcher={
                1:'EURO',
                2:'DOLAR',
                3:'BITCOIN',
                4:'PESOS'
             }
        return switcher.get(i, 'oups  la moneda no existe')

    


def run ():
        items = {}
        while True:
            item = input('''
            Ingrese el nombre del prodcuto:

            para factura pulse f 


            
            ''');

            if item.lstrip().rstrip() == str.casefold('f'):
                break
           
            quantity = input('Ingrese la cantidad del producto: ')

            try:
                items[item] = int(quantity)
            except:
                print('El valor Ingresado debe ser numerico')
        
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


