#!/usr/bin/python -d

days=['yesterday', 'today','tomorrow','dayafter']


#print "Give list is {} , {} ,{}, {}".format(days_one,days_two,days_three,days_four)

count=0

for val_days in days:
    index_count=count+1
    days_val_days=val_days[:index_count].swapcase()+val_days[count+1:]
    print days_val_days
    count=count+1

