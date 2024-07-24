#In Python we do have user functions and methods
def A_Function():
    print("A_Function is Called")

A_Function()

#there can be names_list to a function as well

def add_twonumbers(a,b):
    return a+b

print(add_twonumbers(2,4))

#NOW there can be type of parameters to accept key value pairs and list/string like data
def print_names(name, *names_list, **name_dictoionaries):#(simple var,lists,dictionary)
    print("-- Do you know", name, "?")
    print("-- I'm sorry i don't know", name)
    for arg in names_list:
        print(arg)
    print("-" * 40)
    for kw in name_dictoionaries:
        print(kw, ":", name_dictoionaries[kw])
print_names("Luqman", "Yes i know.",
           "Yes I do know Luqman",
           shopkeeper="Luqman",
           person2="Luqman",
           person1="Luqman")
# you can also change type of arguments
def standard_arg(arg):#works at every type of argument when given 
    print(arg)

def pos_only_arg(arg, /):# only accepts argument from position
    print(arg)

def kwd_only_arg(*, arg):# only accepts arguments from arg="some value"
    print(arg)

standard_arg(2)
standard_arg(arg=2)
pos_only_arg(4)
kwd_only_arg(arg=33)
# Next is collision when name and name is repeated it gives error if name is given by keyword and only gives true when name is mentioned once in calling
def foo(name:str,/ ,**kwds):
    return 'name' in kwds

print(foo(1,**{'name': 2}))
# Next are lambda function 
#These are always stored in a storage location and accept only one argument
# can be acessed by writing name of the storage location with argument val in paranthesis
lambda_var=lambda x:x**x
print(lambda_var(3))
#gives metadata about variable type of parameters when mentioned
print(foo.__annotations__)
#defines class or type used in this case it is function
print(foo.__class__)
#Range is a type of builtin functions that returns list of values
Range=range(2,16,2)#range(from,To+1,how much increament)
for i in Range:
    print(i)