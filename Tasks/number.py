#!/usr/bin/python
# Find grater number in 3 number  and if all three are same print all number equal


num1=input("Print number 1 : ")
num2=input("Print number 2 : ")
num3=input("Print number 3 : ")

###### Logic via IF variables

if(num1 > num2 and num1 > num3):
        print "Number 1 is greter : {}".format(num1)
elif(num2 > num3 and num2 > num1):
        print "Number 2 is grater: {}".format(num2)
elif(num3 > num1 and num3 > num2):
        print "Number 3 is grate : {}".format(num3)
else:
        print "All Threee number are equal:  {}".format(num1)