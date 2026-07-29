# 1.
name = "Pavan"
age = 19
height = 5.8
is_student = True
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Student:", is_student, "| Type:", type(is_student))
'''
Name: Pavan | Type: <class 'str'>
Age: 19 | Type: <class 'int'>
Height: 5.8 | Type: <class 'float'>
Student: True | Type: <class 'bool'>
'''

# 2.
a, b, c = 10, 20, 30
print("a =", a)
print("b =", b)
print("c =", c)

a = b = c = 100
print("\nAfter assigning the same value:")
print("a =", a)
print("b =", b)
print("c =", c)

'''
a = 10
b = 20
c = 30

After assigning the same value:
a = 100
b = 100
c = 100
'''

#3a.
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("\nAfter swapping:")
print("a =", a)
print("b =", b)

'''
Before swapping:
a = 10
b = 20

After swapping:
a = 20
b = 10
'''

#3b.
a = 10
b = 20

print("Before swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter swapping:")
print("a =", a)
print("b =", b)

'''
Before swapping:
a = 10
b = 20

After swapping:
a = 20
b = 10
'''

#4.
value = 100
print("Value:", value)
print("Type:", type(value))

value = "Hello Python"
print("\nValue:", value)
print("Type:", type(value))
'''
Value: 100
Type: <class 'int'>

Value: Hello Python
Type: <class 'str'>
'''