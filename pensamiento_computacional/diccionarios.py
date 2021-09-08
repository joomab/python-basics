my_dict = {
    'David': 20,
    'Erika':30,
    'Jose': 34
    }

print(my_dict.items())

print(my_dict['David'])

print(my_dict.get('Hola', -1)) #Debido a que no existe la llave Hola, con la función .get() podemos definir un valor default, en este caso nos retorna -1

del my_dict['David'] #eliminamos el valor y la llave de David

print(my_dict)

print('Jose' in my_dict) #Retornará True porque si existe en el diccionario
print('Tom' in my_dict) #Retornará False porque Tom no existe en el diccionario
