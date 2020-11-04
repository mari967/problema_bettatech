    #Los strings ya son listas de caracteres
    #Símbolo abierto [{( se agrega a la pila
    #Símbolo cerrado )}]-> se llama a pop para quitar su par abierto, si está en el tope de la pila
    #Si no está su par, entonces la secuencia es incorrecta

def validarSecuencia(secuencia):

    pila = []
    for i in range(len(secuencia)):
        if esSimboloAbierto(secuencia[i]):
            pila.append(secuencia[i])
        elif esSimboloCerrado(secuencia[i]):
            if simboloCoincideConTope(pila, secuencia[i]):
                pila.pop()
            else:
                return "INCORRECTO"
        else: 
            return "INCORRECTO"

    if pila == []:
        return "CORRECTO"
    else: return "INCORRECTO"
    
def esSimboloAbierto(simbolo):
     return simbolo in "{[("

def esSimboloCerrado(simbolo):
    return simbolo in ")]}"

def simboloCoincideConTope(pila, simbolo):

    parDeSimbolo = {
        "}": "{",
        "]": "[",
        ")": "("
    }

    if pila == []:
        return False;
    return parDeSimbolo.get(simbolo) == pila[-1]
    

if __name__ == "__main__":
    
    while(True):
        secuencia = input("Ingrese su secuencia de {][]():\n")
        print(validarSecuencia(secuencia))
