#!/usr/bin/python

numbers=raw_input("Enter three values by space seprate : ")
number_in_list=numbers.split()
print number_in_list

print(type(number_in_list[0]))

if (number_in_list[0] > number_in_list[1]) and (number_in_list[0] > number_in_list[2]):
        print "large number is {}".format(number_in_list[0])
elif (number_in_list[1] > number_in_list[2]) and (number_in_list[1] > number_in_list[0]):
        print "large number is {}".format(number_in_list[1])
elif (number_in_list[2] > number_in_list[1]) and (number_in_list[2] > number_in_list[0]):
        print "large number is {}".format(number_in_list[2])
#else:
#     print "all number equal {}".format(number_in_list[0])


