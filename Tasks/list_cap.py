#!/usr/bin/python


days=['yesterday', 'today','tomorrow','dayafter']

days_one=days[0]
days_two=days[1]
days_three=days[2]
days_four=days[3]

print "Give list is {} , {} ,{}, {}".format(days_one,days_two,days_three,days_four)


format_days_one=days_one[0].swapcase()+days_one[1:]
format_days_two=days_two[:2].swapcase()+days_two[2:]
format_days_three=days_three[:3].swapcase()+days_three[3:]
format_days_four=days_four[:4].swapcase()+days_four[4:]

print "Your Output is :-  \n{}, \n{} ,\n{} ,\n{} ".format(format_days_one,format_days_two,format_days_three,format_days_four)



#print days_one[0].swapcase()
