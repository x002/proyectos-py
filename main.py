#x = int (input ('defina x: '))
# if x % 2 == 0:
#    if x % 3 == 0:
#        print('divisible by 2 and 3')
#    else:
#        print('DISIVSIBLE BY 2 AND NOT BY 3')
#elif x % 3 == 0:
#    print('divisible by 3 and not by 2')

#else:
#    print('divisible by none')

# -------------------------------------

#var = 5
#tipo = type(var).__name__
#srt = str(tipo) 
#print('la variable es de tipo: '+ tipo + ' y contiene un: ' + str(var))

#--------------------------------------
#num = int(input('ingrese un número: '))
#if num == 0:
#    print('Es cero')
#elif num % 2 == 0:
#    print('Es par')
#elif num % 2 != 0:
#    print('Es impar')

#--------------------------------------

#s = "snlkdndlncufndoai"
#vocales = "aeiou"
#count = 0
#for char in s:
#    if char in vocales:
#        count += 1

#print('Number of vowels: ' + str(count))

#----------------------------------------
# s = "sjbobssjbobobsjs" 
# count = 0
# for char in range(0, len(s)-2):
#    if s[char] == "b":
#        if s[char +1] == "o":
#            if s[char +2] == "b":
#                count += 1
    
# print('Number of times bob occurs is: ' + str(count))

#------------------------------------------

# s = "yayeaknbpwjuihdepzhuwr"
# cadena = ""
# letra = ""

# for char in range(len(s) - 1):
#     val1 = ord(s[char])
#     val2 = ord(s[char+1])
#     if char == len(s) - 2:
#         if s[char] <= s[char+1]:
#             cadena = cadena + s[char]
#             if s[char + 1] >= s[char]:
#                 cadena = cadena + s[char + 1]
    
#     elif s[char] <= s[char+1]:
#         cadena = cadena + s[char]
#     else:
#         cadena = cadena + s[char] + " "
        
# lista = cadena.split()
# print('Longest substring in alphabetical order is: ' + max(lista, key = len))

#-----------------------------------------

# arr = [2, 8, 9, 0]
# if len(arr)==1:
#     print('No hay con que comparar')
# else:
#     res = max(arr)-min(arr)
#     print('la diferencia entre el min y el max es: '+ str(res))

#------------------------------------------
# rango = int(input('Ingrese el tamaño del arreglo: ')) ----pendiente.
# print('Ingrese un digito del arreglo de uno a uno.')
# arr = []
# ocurr = 0
# num = 0
# for i in range(rango):
#     n = int(input('número:'))
#     if n == 0 or n < 0:
#         print('no puede ser cero ni negativo.')
#     else:
#         arr.append(n)

# for i in range(rango):
#     ocurr = arr.count(arr[i])
#     if ocurr == arr[i]:
#         num += 1
# print(str(num))

#----------------------------------------

# arr1 = [1,2,2]
# arr2 = [1,6,3]
# num = 0

# for i in range(len(arr1)):
#     if  2>=(abs(arr1[i] - arr2[i])) > 0:
#         num += 1
# print('hay ' + str(num) + ' iteraciones')

#-----------------------------------------
# arr=[]
# res=[]
# start = int(input('Inicio: '))
# end = int(input('Fin: '))
# count = start
# for i in range(end-start):
#     arr.append(count)
#     count += 1
# for i in range(end - start):
#     if arr[i] % 3 == 0 and arr[i] % 5 == 0:
#         arr[i] = 'FizzBuzz'
#     elif arr[i] % 3 == 0:
#         arr[i] = 'Fizz'
#     elif arr[i] % 5 == 0:
#         arr[i] ='Buzz'
# print(arr)

#------------------------------------------

# fila = int(input('cuantas personas son?: '))
# arrFila = []
# arrTurnos=[]
# temp = 0
# con = 0
# for i in range(fila):
#     arrFila.append(i+1)
#     arrTurnos.append(2)
# print(arrFila)

# while(True):
#     cambiante = int(input('Quien va a saltar?: '))

#     if cambiante == 0:
#         for i in range(fila):
#             if (arrFila[i] - (i+1)) > 2:
#                 print('too chaotic')
#                 break
#             elif (arrFila[i] - (i+1)) > 0:
#                 temp = arrFila[i] - (i+1)
#                 con += temp
#                 if (arrFila[i] - (i+1)) == 2 and (arrFila[i+1]-arrFila[i+2])>0:
#                     con += 1    
#         print(str(con))
#     else:
#         if cambiante in arrFila:
#             if arrTurnos[cambiante-1] > 0:
#                 temp = cambiante
#                 indx = arrFila.index(cambiante)
#                 if indx != 0:
#                     arrFila[indx] = arrFila[indx-1] 
#                     arrFila[indx-1] = temp            
#                     arrTurnos[cambiante-1] -= 1
#                     print(arrFila)
#                 else: 
#                     print('ya esta al principio de la fila')
#             else:
#                 print('Ya no le quedan movimientos a este elemento')
#         else:
#             print('Esta persona no existe')

#---------------------------------------------
# import math
# def areas(r, a):
#     """
#     :param r: (float) The radius of the circle.
#     :param a: (float) The angle of the segment.
#     :returns: (list) (A list of two elements containing the area inside, and area outside the circle, in that order.)
#     """
#     pi = math.pi
#     area = pi * (r**2)

#     op2 = (a*(pi/180))-(math.sin(a*(pi/180)))
#     op1 = (r**2)/2
#     segmento = op1 - op2
#     return (area, segmento)

# print(areas(10, 90))


#--------------------------------------------------
# balance = 3200
# balance1 = balance
# rate = 10
# annualInterestRate = 0.2

# mensual = annualInterestRate/12

# while True:
#     balance = balance1
#     for i in range(12):
#         balance = balance - rate
#         balance = balance + (mensual * balance)
#     if balance <= 0:
#         break
#     else:
#         rate += 10

# print ('Lowest Payment: '+ str(rate))

#------------------------------------------------
# import math
# def polysum(n,s):
#     def areaPol(n,s):
#         area = (0.25 * n * s ** 2)/math.tan(math.pi/n)

#         return area
#     def periPol(n,s):
#         perimetro = n * s

#         return perimetro

#     sum = areaPol(n,s) + (periPol(n,s) ** 2)

#     return round(sum,4)
#-----------------------------------------------


 