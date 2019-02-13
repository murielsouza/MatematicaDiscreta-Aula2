a = {1, 2, 3, 4}
b = {2, 3, 4, 5}

#Cria os conjuntos A e B
set(a)
set(b)

#uniao A B
u = a.union(b)
print (u)

#interseção A B
i = a.intersection(b)
print (i)

#Diferença A B
d = a.difference(b)
print(d)

#diferença simétrica A B
s = a.symmetric_difference(b)
print (s)

#verificando subconjunto A B
p = a.issubset(b)
print (p)