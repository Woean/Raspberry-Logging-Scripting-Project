#!/usr/bin/python3

#stores values from file to list parsed to floats
try:
    with open('humidityvalues.txt') as f:
        lines = [float(line.rstrip()) for line in f]
except:
    print("error reading file")

#sorts list
lines.sort()

print ("Lowest measured humidity during last 50 measurements: ",lines[0],"%")
print ("Highest measured humidity during last 50 measurements: ",lines[49],"%")

#calculates average
def Average(lst):
    return sum(lst) / len(lst)

average = Average(lines)

print ("Average measures humidity within last 50 measurements: ",round(average,2),"%")




