t=("india","russia","japan","australia","south africa","israel")
for i in t:
    print(type(i),"length: ",len(i))

r=(2,)
print(type(r[0]))


p=tuple(["india","russia","japan","australia","south africa","israel"])
l=list(("india","russia","japan","australia","south africa","israel"))
print(type(p))
print(type(l))