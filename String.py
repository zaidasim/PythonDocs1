String="    MY name Is zaid and Is"
length=len(String)# calculates length and store in a variable
print(length)
String=String.lower()#converts all characters to small case
print(String)
String=String.title()#converts each word's starting to capitalize
print(String)
String=String.strip()#remove wide space i.e more that one space from word/String
print(String)

splitstring=String.split()# makings a list of all the words in the string
print(splitstring)
findindex=String.find("Is")#lowest index that has the substring occurences
print(findindex)
findindex1=String.rfind("Is")#highest index that has the substring occurences
print(findindex1)
counting=String.count("Is")# counting number of time a string occured
print(counting)
String1=String.replace("Is","is",1)#replaces word with another , 3rd parameter is optional and it is saying how many occcurances
print(String1)

print(String.startswith("My"))#returns true if the string starts with the word mentioned
print(String.endswith("My"))#returns true if the string ends with the word mentioned

print(String.isalpha())#returns true if the string is all alphabetic 
print(String.isdigit())#returns true if the string is all digits
print(String.isalnum())#returns true if the string is all alphanumeric
print(String.isspace())#returns true if the string is all space

print(String.istitle())#returns true if the string is in title case i.e Title
print(String.swapcase())#Swaps case of string