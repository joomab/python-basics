a = [1,2,3]
b = a #van a tener el mismo id
print(id(a))
print(id(b))
c = list(a) # genera un nuevo id
print(id(c))

d = a[::] # clonar una lista con método de slices
print(id(d)) # genera un nuevo id, no es el mismo de a y b