""" 
Recibir un numero en teclado y determinar si este es múltiplo de 5
Recibir un numero en teclado y determinar si este es múltiplo de 3

 """

numeroM5 = int(input(' Digita un numero para determinar si es multipo de 5: ')) 
print('-----------------------------------------------------------------------------')
numeroM3 = int(input(' Digita un numero para determinar si es multipo de 3: ')) 

def determinarMultiplo(parametro):
    resultado=None
    if parametro == numeroM5:
        if parametro%5!=0:
            resultado= str(parametro)+' no es multiplo de 5'
        else: 
            resultado= str(parametro)+' SI es multiplo de 5'
    elif parametro == numeroM3:
        if parametro%3!=0:
            resultado= str(parametro)+' NO es multiplo de 3'
        else:
            resultado= str(parametro)+' SI es multiplo de 3'
    return resultado    

print('-----------------------------------------------------------------------------')

print(determinarMultiplo(numeroM5)) 
print(determinarMultiplo(numeroM3)) 


         

        

    