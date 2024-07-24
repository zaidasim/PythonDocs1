# Python consists of various numbers , Strings and data structures some data manipulation operators are discussed here
k=5
m=3
mn=True
nm=False
print(mn or nm)#or operator
print(nm and mn)#and operator
print(not nm)# not operator
print(k+m) #add k and m
print(k-m)#subtracts m from k
print(k*m)#k multiplies m
n=k/m
print(n)#k divided by m and stored in n
print(k//m)#k floor division by m 

#Built-in Functions for Numbers
float(n)#converts n which is float in string
print(n)#prints n
round(n,4)
print(n)#prints n
print(pow(4,2))#16
print(divmod(k,m))#gives a tuple containing Quotient and remainder
import math
print(math.ceil(k))# give imediate integer greater than k
print(math.log(k,m))#prints log k to base m  
print(math.exp(k))#returns exponential to the power of k
print(math.sin(k),math.cos(k),math.tan(k))# prints sin cos and tan of k