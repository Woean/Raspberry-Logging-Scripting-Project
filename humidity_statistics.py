with open('humidityvalues.txt') as f:
    lines = [float(line.rstrip()) for line in f]

lines.sort()

print ("Lowest measured humidity during last 50 measurements: ",lines[0],"%")
print ("Highest measured humidity during last 50 measurements: ",lines[49],"%")

def Average(lst):
    return sum(lst) / len(lst)

average = Average(lines)

print ("Average measures humidity within last 50 measurements: ",round(average,2),"%")




