#variables in python
#IN PYTHON VARIABLES ARE DECLARED WITHOUT DATATYPE
x=10; #this is a variable which containes the value
# python is case sensitive

#data types in python
# 1.numeric type  int → whole numbers
#                 float → decimal numbers
#                 complex → used in advanced math

#2.string  immutale(cannot be changed directly) 
#3.boolean
#4. list,tuple,set,dictionary

#input in python
name=input("enter your name : ")  #this metgod always return string whether you enter numeric value
print(name)
age=int(input("enter the agee : ")) #this can change the type of input from string to int
print(age)

#TYPE CASTING
#converting one data type to another
#1.implicit this is automatic type conversion and converts small data type to large 
#2.explicit this is manual tyle which is used to convert large data type to smaller

#implicit
p=10
y=2.5
print(p+y)

#explicit
r="10"
s=int(x)
print(s+5)
