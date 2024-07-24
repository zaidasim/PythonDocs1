#if Else
c="This is if else"
if c=="NOT ":
    print("Au Ho")
else:
    print("Mughe pta ha ye if else ha")
#if elif else
d="This is if elif and else"
value=909
if value<65:
    print("hmm")
elif value==0:
    value="cd"
else:
    print("Ma ni btau ga")
#Nested if
if 999<8888:
    
    if "ll">"yyy":
        pass
    else:
        print("<<")
#Different Orientation of if else
is_odd=["YES" if 2%2==0 else "NO"]
print(is_odd.pop())
print("========MatchCase========")
#simple Match Case:
match (66-9):
    case 1:
        print(",")
    case 57:
        print("Fifty Seven")
    case _:
        print("kuch ni")
#Without Default:

match(8**2):
    case 64:
        print("8X8:64")

#Nested Match case
match(2-1):
    case 1:
        match 44-33:
            case 11:
                print("Eleven")
