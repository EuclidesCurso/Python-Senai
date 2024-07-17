# importando biblioteca randômica 

import random

# definir o tamanho da matriz
TAM = 3

# Definido um laço para a matriz que  # inteira TAM vezes
mat1 = [[] for _ in range (TAM)] 
mat2 = [[] for _ in range (TAM)] 
mat3 = [[0 for _ in range (TAM)] for _ in range (TAM)]

#preenchendo a matriz com numeros aleatorios
# de forma mais complexa
# def soma():
   # for lin in range(TAM):
    #    soma_lin = []
     #   for col in range(TAM):
      #      soma_lin.append(mat1[lin][col]+mat2[lin][col])
       #     mat3[lin]=soma_lin

#MAIS curta
def soma():
    for lin in range(TAM):
        for col in range(TAM):
            mat3[lin][col] = mat1[lin][col] + mat2[lin][col]

def sub():
    for lin in range(TAM):
        for col in range (TAM):
            mat3[lin][col] = mat1[lin][col] - mat2[lin][col]

def mult():
    for lin in range(TAM):
        for col in range (TAM):
            mat3[lin][col] = mat1[lin][col] * mat2[lin][col]

#def div():
 #   for lin in range(TAM):
  #      for col in range (TAM):
   #         mat3[lin][col] = mat1[lin][col] / mat2[lin][col]


for lin in range(TAM):
    for col in range(TAM):
        mat1[lin].append(random.randrange(0,10))
        mat2[lin].append(random.randrange(0,10))

#para exibir
print('Matriz 1: ')
for linha in mat1:
    print(linha)

#linha nesse caso virou um contador
print('Matriz 2')
for linha in mat2:
    print(linha)

print('Matriz soma: ')
soma()
for linha in mat3:
    print(linha)

print('Matriz subtração: ')
sub()
for linha in mat3:
    print(linha)

print('Matriz multiplicação: ')
mult()
for linha in mat3:
    print(linha)

#print('Matriz divisão: ')
#div()
#for linha in mat3:
 #   print(linha)