#WHILE
Counter=3
while True:
    if Counter>0:
        print(f"While Counter= {Counter}\n")
        Counter=Counter-1
    else:
        break
    
#Nested While
while "A"=="A":
    if Counter< 3:
        while "b"=="b" or Counter<3:
            print(f"While Counter= {Counter}\n")
            Counter=Counter+1
            break
    else:
        print("Complete")
        break
#for loop
for_var="This is for for loop"
counter1=len(for_var)
counter2=counter1//2
for var in for_var:
    if counter1>counter2:
        print(f"{var}\t")
        counter1=counter1-1
        
    
    else:break
    
#nested for
for i in range(0,4):
    for j in range(i,i+1):
        print(f"{i} and {j}")


        
            
        
    
        
