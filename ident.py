#1.
age = 20
MAX_LIMIT = 100
def greet():
    return "Hello"
class Student:
    pass
student_name = "Pavan"
print("Variable:", age)
print("Constant-style name:", MAX_LIMIT)
print("Function name:", greet())
print("Class name:", Student.__name__)
print("Identifier with underscore:", student_name)

'''
Variable: 20
Constant-style name: 100
Function name: Hello
Class name: Student
Identifier with underscore: Pavan
'''

#2.
2value        #SyntaxError: invalid decimal literal
value_2        #valid
_hidden     #valid
class           #SyntaxError: invalid syntax
my-var=6        #SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
MyClass  =0    #valid
total$       #SyntaxError: invalid syntax
'''
'''

#3.
Marks = 95
marks = 80

print("Marks =", Marks)
print("marks =", marks)
'''
Marks = 95
marks = 80
'''