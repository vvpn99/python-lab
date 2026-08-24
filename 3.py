print("enter lengths of sides = ")
a = int(input())
b=int(input())
c=int(input())
if (a>0 and b>0 and c>0):
    if(a+b>c or b+c>a or c+a>b):
        if(a==b==c):
         print("equilateral triangle")
        elif b==c and a!=b:
            print("isosceles triangle")
        else:
            print("scalene triangle")
    else:
        print("not a valid triangle")
        
