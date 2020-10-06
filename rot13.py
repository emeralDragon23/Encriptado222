#///d4nt3_c//// for SoloLearn
#Rot13, es un estandar para el cifrado Cesar
#Por lo tanto cada letra del alfabeto latino se corren 13 letras hacia lante'.
#formula f(n)=n+13 si 1<=n<=13, f(n)=n-13 si 14<=n<= 26
#alfabeto.
#for des-encrypt https://www.rot13.com/

valores = { 'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,
            'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,
            'q':17, 'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,
            'y':25,'z':26, '_':0}

def diccionario_inverso(diccionario):

    reverse = {}

    for kei in diccionario:
        
        reverse[diccionario.get(kei)] = kei
    
    return reverse

def codificacion(entrada,diccionario):

    salida = []
    
    for caracter in entrada:

        salida.append(diccionario.get(caracter))

    return salida

def encriptacion(texto_codificado):

    salida = []
    aux = 0

    for iterador, digito in enumerate(texto_codificado):
        #formula f(n)=n+13 si 1<=n<=13, f(n)=n-13 si 14<=n<= 26
        
        try:    
            if 0 <= digito <= 13:

                aux = texto_codificado[iterador] + 13
                salida.append(aux)
        
            elif 14 <= digito <= 26:
                aux = texto_codificado[iterador] - 13
                salida.append(aux)
        except:

            aux = 0
            salida.append(aux)

    return salida

def texto_encriptado(encriptacion, diccionario_inverso):

    salida = ""

    for digito in encriptacion:

        salida += diccionario_inverso.get(digito)

    return salida

valores_inversos = diccionario_inverso(valores)

entrada = " ".join(input('Encrypted $> ').lower()).split(" ")

print(texto_encriptado(encriptacion(codificacion(entrada, valores)), valores_inversos))





