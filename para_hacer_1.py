import os

myNumber = 'Rafael Fernandez'
myName = 42 

#se limpia la pantalla
os.system('cls')

#intercambio de variables
print("programa intercambio de variables")
cond = True
while cond:
    pivote = myNumber
    
    myNumber = myName
    myName = pivote
    
    print("Variable myName : ",myName,flush=True)
    print("Variable myNumber : ",myNumber,flush=True)
    
    continuar = input("\nDesea continuar S/N ?   ")
    continuar = continuar.strip()
    cond = continuar == "S" or continuar == "s"
        
print("\nfin del programa!S\n")
print("Variable myName : ",myName,flush=True)
print("Variable myNumber : ",myNumber,"\n",flush=True)

print("presione una tecla para continuar...",end="")
input("...")

#se limpia la pantalla
os.system('cls')


#rango de -52 hasta 1066
print("programa que imprime secuencia entre -52 y 1066\n")

print("presione una tecla para continuar...",end="")
input("...\n")

for i in range(-52,1067):
    print(i,flush=True, end="")
    if i < 1066: print(" , ",end="")

print("\n\npresione una tecla para continuar...",end="")
input("...")



#se limpia la pantalla
os.system('cls')

#iimpresion 98 veces
print("programa que imprime 'buenos dias' 98 veces\n")

print("presione una tecla para continuar...",end="")
input("...\n")


def beCheerful():
    print("\n")
    for i in range(1,99):
        print(i,"buenos dias",end="")
        if i < 98: print(" , ",end="")


#se invoca a la funcion
beCheerful()
print("\n\npresione una tecla para continuar...",end="")
input("...")


#se limpia la pantalla
os.system('cls')

#multiplos de 3 entre -300 y 0, menos -6 y 03
print("programa que imprime los multiplos de 3 entre -300 y 0 exceptuando -6 y -3\n")

print("presione una tecla para continuar...",end="")
input("...\n")


for i in range(-300,1):
    if i % 3 == 0:
        if i != -6 and i != -3:
            print(i," es multiplo de 3",end="")
            if i < 0: print(" , ",end="")


print("\n\npresione una tecla para continuar...",end="")
input("...")


#se limpia la pantalla
os.system('cls')

#imprime numeros enteros con while entre 2000 y 5280
print("programa que imprime numeros enteros con while\n")

print("presione una tecla para continuar...",end="")
input("...\n")

i = 2000
while i <= 5280:
   print(i, end="")
   if i < 5280: print(" , ",end="")
   i+=1


print("\n\npresione una tecla para continuar...",end="")
input("...")


#se limpia la pantalla
os.system('cls')

#mes y ano de nacimiento
print("programa que confirma mes o ano de nacimiento\n")
print("presione una tecla para continuar...",end="")
input("...\n")

nacimeinto_mm_yyyy = ['1', '2000']

numero1 = str(int(input("introduzca el primero numero : ").strip())).strip()
numero2 = str(int(input("introduzca el segundo numero : ").strip())).strip()

if numero1 in nacimeinto_mm_yyyy and numero2 in nacimeinto_mm_yyyy:
    print("\ncomo lo supiste...")
else:
    print("\nun dia cualquiera")


print("\n\npresione una tecla para continuar...",end="")
input("...")


#se limpia la pantalla
os.system('cls')

#bisiesto
print("programa que verifica si un ano es biciesto\n")
print("presione una tecla para continuar...",end="")
input("...\n")

year_confirm = int(input("intrduzca el año que desea comprobar : ").strip())

if year_confirm % 4 != 0: #no divisible entre 4
	print("No es bisiesto")
elif year_confirm % 4 == 0 and year_confirm % 100 != 0: #divisible entre 4 y no entre 100 o 400
	print("Es bisiesto")
elif year_confirm % 4 == 0 and year_confirm % 100 == 0 and year_confirm % 400 != 0: #divisible entre 4 y 10 y no entre 400
	print("No es bisiesto")
elif year_confirm % 4 == 0 and year_confirm % 100 == 0 and year_confirm % 400 == 0: #divisible entre 4, 100 y 400
	print("Es bisiesto")
 
print("\n\npresione una tecla para continuar...",end="")
input("...")


#se limpia la pantalla
os.system('cls')

#multiplos de 5 entre 512 y 4096
print("programa que imprime los multiplos de 5 entre 512 y 4096\n")

print("presione una tecla para continuar...",end="")
input("...\n")

contador = 0
for i in range(512,4097):
    if i % 5 == 0:
        contador+=1
        print(i," es multiplo de 5",end="")
        if i < 4095: print(" , ",end="")

print(f"\n\nen total se contaron {contador} numeros que eran multiplos de 5 entre 512 y 4096")

print("\n\npresione una tecla para continuar...",end="")
input("...")


#se limpia la pantalla
os.system('cls')

#imprime numeros enteros con while entre 2000 y 5280
print("programa que cuentas los multiplos de 6 entre 0 y 60000 usando while \n")

print("presione una tecla para continuar...",end="")
input("...\n")

i = 0
while i <= 60000:
   if i % 6 == 0:
       print(i," es multiplo de 6", end="")
       if i < 60000:
           print(" , ",end="")
   i+=1


print("\n\npresione una tecla para continuar...",end="")
input("...")



#se limpia la pantalla
os.system('cls')

#contando a la manera de coding dojo
print("programa que cuenta a la manera de coding dojo\n")

print("presione una tecla para continuar...",end="")
input("...\n")

for i in range(1,101):
    if i % 5 == 0:
        print(" codificando",end="")
        if i % 10 == 0:
            print(" dojo",end="")
    else:
        print(i,end="")

    if i < 100: print(" , ",end="")

print("\n\npresione una tecla para continuar...",end="")
input("...")

#se limpia la pantalla
os.system('cls')

#contando a la manera de coding dojo
print("programa que sabes\n")

print("presione una tecla para continuar...",end="")
input("...\n")

def quesabes(parametro=""):
    print(parametro,end="\n")

quesabes("\nimprime que sabes...\n")

print("\n\npresione una tecla para continuar...",end="")
input("...")


#se limpia la pantalla
os.system('cls')

#contando a la manera de coding dojo
print("programa guao es un numero grande\n")

print("presione una tecla para continuar...",end="")
input("...\n")

acumulador = 0
for i in range(-300,301):
    print(i % 2,end="")
    if i % 2 != 0:
        acumulador+= i
    if i < 300: print(" , ",end="")

print("\n\nla suma es : ",acumulador,end="\n")

print("\n\npresione una tecla para continuar...",end="")
input("...")


#se limpia la pantalla
os.system('cls')

#contando a la manera de coding dojo
print("\nprograma cuenta regresiva cada 4\n")

print("presione una tecla para continuar...",end="")
input("...\n")

numero = 2016
while numero >= 1:
    print(numero,end="")
    numero-=4
    if numero > 1: print(" , ",end="")


print("\n\npresione una tecla para continuar...",end="")
input("...")



#se limpia la pantalla
os.system('cls')

#contando a la manera de coding dojo
print("\nprograma cuenta regresiva flexible\n")

print("presione una tecla para continuar...",end="")
input("...\n")

low_num = 2
high_num = 9
mult = 3

for i in range(low_num,high_num+1):
    if i % mult == 0:
        print(i,end="")
        if i < high_num: print(" , ",end="")


print("\n\npresione una tecla para continuar...",end="")
input("...")




#se limpia la pantalla
os.system('cls')

#contando a la manera de coding dojo
print("\nprograma cuenta regresiva final\n")

print("presione una tecla para continuar...",end="")
input("...\n")

param1 = -100
param2 = 100
param3 = 3
param4 = 69

for i in range(param1,param2+1):
    if i % param3 == 0:
        if i != param4:
            print(i,end="")
            if i < param2: print(" , ",end="")


print("\n\npresione una tecla para continuar...",end="")
input("...")