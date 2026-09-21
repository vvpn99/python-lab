t={1:"sree",2:"jan",3:"nihan",4:"rama",5:"chinna"}
print(t.keys())
print(t.values())
print(t.items())



print(t.pop(3))
print(t.get(5))


if t.get(5) is not None:
    del t[5]
    
print(t)


i=int(input("k:"))
if i in t.keys():
 print(t[i])
else:
    print(None)
    
    
    

t={1:"sree",2:"jan",3:"nihan"}
u={4:"rama",5:"chinna"}
m=t.copy()
m.update(u)
print(m)
m=t|u
print(m)

v={"onion":70,"tomato":30,"potato":20}
print(max(v.values()))
print(min(v.values()))




f=input("enter string : ")
d={}
for i in f:
   d[i]=d.get(i,0)+1
print(d)



c={x:x**x for x in range(1,11)}
print(c)
    
    
    
    
    

