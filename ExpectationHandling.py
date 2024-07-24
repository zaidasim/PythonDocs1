
#To handle different types of errors we use try and expect
while True:
    try:
        x = int("33f")
        break
    except ValueError:
        print("Try again...")
        break
#The raise statement allows the programmer to force a specified exception to occur
try:
   print("try")
finally:
    print('finally')
#the finally will run before try weather or not it becomes true 
