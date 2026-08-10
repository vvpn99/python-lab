#B1

a=23
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
'''
29
17
138
3.8333333333333335
3
5
148035889
'''

#B2

m=int(input("enter m :"))
n=int(input("enter n :"))
print(m==n)
print(m!=n)
print(m<n)
print(m>n)
print(m<=n)
print(m>=n)
'''
enter m :45
enter n :67
False
True
True
False
True
False
'''

#B3.

s=50
print(s)
s+=50
print(s)
s-=50
print(s)
s*=50
print(s)
s/=50
print(s)
s//=50
print(s)
s%=50
print(s)
s**=50
print(s)
'''
50
100
50
2500
50.0
1.0
1.0
1.0
'''

#B4.

percent =int (input("enter percentage :"))
a=int(input("enter attendance : "))
if percent>=75 and a>=90:
    print("eligibility for scholarship : ","eligible")
else:
    print("eligibility for scholarship :","not eligible")
'''
enter percentage :90
enter attendance : 90
eligibility for scholarship :  eligible
'''

#B5.

p=12
q=10
print(bin(p),bin(q))
print(p&q)
print(p|q)
print(p^q)
print(~p)
print(p<<2)
print(p>>2)
'''
0b1100 0b1010
8
14
6
-13
48
3

'''

#B6.

f=["apple","banana","cherry","grape","kiwi"]
item =input("enter a fruit : ");
print(item in f ,"is in the list ")
print(item not in f," is not in th list")
'''
enter a fruit : apple
True is in the list 
False  is not in th list
'''

#b7.

l1 =[1,2,3]
l2 =[1,2,3]
l3 = l1
print(l1==l2)
print(l1 is l2)
print(l1 is l3)
print(id(l1),id(l2),id(l3))
'''
True
False
True
2848710869568 2848710869952 2848710869568
'''