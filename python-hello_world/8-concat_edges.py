#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
#str = str[45:72]+" "+str[88:92]+" "+str[0:6]
print(str[45:71] + str[88:91] + str[0:6].replace("Python", " Python"))
