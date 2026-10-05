
import os , subprocess

comando = 'cls' if os.name == 'nt' else 'clear'
subprocess.run(comando, shell=True)

num1 = int(input('Ingrese el Primer numero:'))
num2 = float(input('Ingrese el Segundo numero:'))

suma = num1 + num2

print (f'El resultado entre {num1} y {num2} es {suma}')
