#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = f"{str.split(' ')[5]} " +  f"{str.split(' ')[6]} " +  f"{str.split(' ')[12]} " +  f"{str.split(' ')[0]} "
print(str)
