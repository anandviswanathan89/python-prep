#find integers in string
import re
a = "ANAND IS 1 2 A 3 4 GOOD BOY 3243"
temp = re.findall('[0-9]+', a)
print(temp) #['1', '2', '3', '4', '3243']

#sum of all integers
b = [int(i) for i in temp]
print(sum(b)) #3253


#find if it is ip
