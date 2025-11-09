
Variable = input ('te gustaria declarar variables conmigo')
print (Variable) 

1
print('Hola')
name = 'Pepe'
print('Hola', name)
print('Si cambias de valor entonces puede pasar a valor de salida u entrada o a uno especia')
print('Hola', name, sep=' ')

2
name = input ("¿Cómo te llamas? ")
print( "Hola " + name)


3
fechaNacimiento = int(input("¿En que año naciste? "))
edad = 2025- fechaNacimiento
print("Tu edad es ",edad)

4
                                
s = input('Introduzca un número entero: ')
try:
    valorInt = int(s)
    print('Es entero')
except:
    print('No es entero')

print('Hemos terminado')

5
                                           

a = input("Introduce el primer número: ")
b = input("Introduce el segundo número: ")

suma_cadenas = a + b
print("Suma como cadenas:", suma_cadenas)

suma_numeros = int(a) + int(b)
print("Suma como números:", suma_numeros)

6  

a = int(input("Introduce el primer número (a): "))
b = int(input("Introduce el segundo número (b): "))


print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)     
print("a // b =", a // b)  
print("a % b =", a % b)     
print("a ** b =", a ** b)   

a_original = a
a += b
print("Después de 'a += b', a pasa de", a_original, "a", a)

7

palabra = input('Introduzca una palabra')
print('la palabra: ' + palabra + ' mide ')
print(len(palabra))

8 


frase = input("Escribe una frase con espacios al principio y al final: ")


print("Frase original: [" + frase + "]")


frase_sin_espacios = frase.strip()

print("Con strip(): [" + frase_sin_espacios + "]")


print("En minúsculas:", frase_sin_espacios.lower())


print("En mayúsculas:", frase_sin_espacios.upper())

9


nombre = "Pepe"
edad = 20


print(f"{nombre} tiene {edad} años.")


valor1 = 1.45
valor2 = 45.45

print(f"{valor1:6.3f}")
print(f"{valor2:6.3f}")

10

print("Tres emojis usando códigos Unicode:")

emoji_perro = chr(0x1F415)   
emoji_mundo = chr(0x1F30E)   
emoji_ordenador = chr(0x1F5A5)  

print(emoji_perro, emoji_mundo, emoji_ordenador)
