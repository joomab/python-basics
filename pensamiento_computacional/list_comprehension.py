my_list = list(range(100)) # una lista de 0 a 100 [0,1,...99]
print(my_list)

#doblamos cada valor de la lista

double = [i * 2 for i in my_list] #Esto es una list comprehension
print(double)

#ahora queremos sacar solo los valores pares de my_list

pares = [i for i in my_list if i%2 == 0]
print(pares)