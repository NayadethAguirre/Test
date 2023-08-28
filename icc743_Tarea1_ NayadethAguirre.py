print("--------------- PRUEBA DIAGNOSTICO ICC743 ---------------")
print("Nombre: Nayadeth Aguirre Villegas ")
print("Carrera: Ing. Civil Telemática ")
print("Matricula:19104053817 ")



#Ejercicio 1 
#Escriba un programa que calcule la suma de todos los números naturales pares menores que 1000.
print("--------------- Ejercicio 1 ---------------")
n=1000
aux=0
for i in range(n) :
    if (i%2==0):
        aux+=i
print("La suma de todos los números naturales pares menores a 1000 es:",aux)


#Ejercicio 2
#Dada la siguiente lista de números, escriba un programa que genere una nueva lista que contenga solo los números mayores que el promedio de la lista original.
print("--------------- Ejercicio 2 ---------------")
numeros = [45,67,23,89,12,56,78,90,34,67]
prom=sum(numeros)/len(numeros)
listAux=[]

for i in range (len(numeros)):
    if(numeros[i]>prom):
        listAux.append(numeros[i])

print("El promedio de la lista entregada es :",prom)
print("Lista Nueva",listAux)

#Ejercicio 3
#Escriba una función que tome como entrada una cadena de texto y devuelva el número de palabras en la cadena.

print("--------------- Ejercicio 3 ---------------")

def contar_palabras(texto):
    countWords=0
    listWords=[]
    text=texto.split()
    for i in range (len(text)):
          if(len(text[i])!=1):
               listWords.append(text[i])
    countWords=len(listWords)
    return countWords

# Ejemplo de uso:
texto = "La ciencia de datos es emocionante y desafiante."
print("El número de palabras es :",contar_palabras(texto))  # Debería imprimir: 7


#Ejercicio 4
#Dado un diccionario con nombres y edades, escriba un programa que imprima el nombre de la persona más joven.   
print("--------------- Ejercicio 4 ---------------")

personas = {
    "Juan": 25,
    "María": 30,
    "Carlos": 22,
    "Ana": 28
}

masJoven = min(personas, key=lambda x: personas[x])
print("El nombre de la personas más joven es: ",masJoven)

#Ejercicio 5
    #Escriba un programa que lea un archivo de texto llamado "datos.txt" que contiene números separados por espacios (use los datos que estime pertinente), y calcule la suma de todos los números en el archivo.
print("--------------- Ejercicio 5 ---------------")
listDatos = []
with open('datos/datos.txt', 'r') as datos:
    numeros_str = datos.read().split()

suma = 0
for numero_str in numeros_str:
    try:
        numero = float(numero_str)
        suma += numero
    except ValueError:
        pass
print("Suma de los números en el archivo datos.txt es :", suma)