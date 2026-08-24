x=int (input("x: "))
for i in range(1,11):
    print(x,"X",i,'=',x*i)
print('\n\n')


f=1
for i in range(1,x+1):
    f*=i
print("the factorial of ",x,"= ",f)
print("\n\n")



y=input("enter text:")
v=0
s=0
n=0
c=0
for i in y:
    if i in "aeiou":
        v+=1
    elif i==" " :
        s+=1
    elif i in "1234567890":
        n+=1
    else:
        c+=1
print("the no. of vowels in given text :",v)
print("the no. of consonants in given text :",c)
print("the no. of spaces in given text :",s)
print("the no. of digits in given text :",n)
print('\n\n')

z=int(input("enter number to know whether it is prime or not:"))
c=0
for i in range(1,z+1):
    if z%i==0:
        c+=1
if c==2:
    print(x, "is prime")
    
l1=int(input("enter limit 1:"))
l2=int(input("enter limit 1:"))
d=0
print("prime numbers : ")
for i in range(l1,l2):
    d=0
    for j in range(1,i+1):
        if i%j==0:
          d+=1
    if d==2:
        print(i  )
    



