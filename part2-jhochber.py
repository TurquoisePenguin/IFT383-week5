#!/usr/bin/python
import math

stringA = input("Enter x1 and y1 for Point 1: ")
stringA = stringA.replace(" ","")
pointA = stringA.split(",")

stringB = input("Enter x2 and y2 for Point 2: ")
stringB = stringB.replace(" ","")
pointB = stringB.split(",")

distance =round(math.sqrt((float(pointB[0])-float(pointA[0]))**2 + (float(pointB[1])-float(pointA[1]))**2),1)
print(f"The distance between ({pointA[0]}, {pointA[1]}) and ({pointB[0]}, {pointB[1]}) is {distance}")
