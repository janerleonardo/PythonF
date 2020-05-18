from textblob import TextBlob

#python -m pip install --up
#pip3 install -U textblob

textEnglish = '''
Hello my name is Janer and I am developing in python
'''
testEspanish = '''
Hola mi nombre es  Janer y estoy desarrollando en python
'''


print(' ')
print('Español')
blob = TextBlob(textEnglish) 
print(blob.translate(to="es"))
print(' ')
print('Ingles')
try:
    blob = TextBlob(testEspanish)
    print(blob.translate(to="en"))
except errorValidad:
    print('La traduccion ya fue hecha')    
