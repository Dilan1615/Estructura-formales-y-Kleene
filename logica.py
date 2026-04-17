def generar_cadenas(alfabeto,max_len):
    resultado = [""] #S

    for i in range(1,max_len+1):
        nuevas = []
        for cadena in resultado:
            for simbolo in alfabeto:
                nueva_cadena = cadena+ simbolo
                nuevas.append(nueva_cadena)
        resultado.extend(nuevas)
    final = []
    for elemento in resultado:
        if elemento not in final:
            final.append(elemento)
    return final




def pertenece (cadena, lenguaje):
    for elemento in lenguaje:
        if elemento == cadena:
            return True
    return False

def union(L1,L2):
    resultado = L1.copy()

    for  elemento in L2:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado
        
def concatenacion(L1,L2):
    resultado = []
    for x in L1:
        for y in L2:
            nueva = x+y
            resultado.append(nueva)
    return resultado

def kleeneStar(L, max_iter):
    resultado = [""]
    actual = [""]

    for i in range(1, max_iter + 1):
        nuevo = []

        for x in actual:
            for y in L:
                cadena = x + y
                nuevo.append(cadena)

        for elemento in nuevo:
            if elemento not in resultado:
                resultado.append(elemento)

        actual = nuevo

    return resultado

def kleenePlus(L,max_iter):
    ks = kleeneStar(L,max_iter)

    resultado =[]
    for elemento in ks:
        if elemento != "":
            resultado.append(elemento)
    return resultado

def tamanio(L):
    return len(L)

def analizar_crecimiento (L):
    for i in range(1,5+1):
        resultado = kleeneStar(L,i)
        print("Iteracion: ",i)
        print("Cantidad: ",tamanio(resultado))
    