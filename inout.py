#1.
n=input("Enter name:")
g=int(input("enter age:"))
print("hello,",n,"you will turn",g+1,"next year")
#2.
a=input("a =")
b=input("b =")
print("sum = ",int(a)+int(b))
print("difference = ",int(a)-int(b))
print("product = ",int(a)*int(b))
print("quotient = ",int(a)/int(b))

#3.
name = "Pavan"
marks = 95

print("Name:", name, "Marks:", marks)

print("Name: {} Marks: {}".format(name, marks))

print(f"Name: {name} Marks: {marks}"

'''
Name: Pavan Marks: 95
Name: Pavan Marks: 95
Name: Pavan Marks: 95
'''
#4.
numbers = input("Enter numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]

print("Sum =", sum(numbers))
#Enter numbers separated by spaces: 10 20 30
#Sum = 60
