y=int(input("enter year : "))
if(y<=0):
    print("invalid")
    
elif ((y%4)==0 and (y%100!=0)):
    print(y ,"is a leap year")
else:
    print(y ,"is not a leap year")
