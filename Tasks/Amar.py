 #!/usr/bin/env python
import sys
_author_ = 'akishore'

days = ['yesterday', 'today', 'tomorrow', 'dayafter']

for Index in days:
   Index_num = days.index(Index)
   day = (days[Index_num])
   count=0
   for inc_count(count=0,count<=4,count=count+1):

   if Index_num == 0:
       day_val = list(day[0:Index_num+1].upper())
       day = list(day)
       for i in range(Index_num+1):
           day[i] = day_val[i]
       limiter = ''
       day = limiter.join(day)
       days[Index_num] = day

   elif Index_num == 1:
       day_val = list(day[0:Index_num+1].upper())
       day = list(day)
       for i in range(Index_num+1):
           day[i] = day_val[i]
       limiter = ''
       day = limiter.join(day)
       days[Index_num] = day

   elif Index_num == 2:
       day_val = list(day[0:Index_num+1].upper())
       day = list(day)
       for i in range(Index_num+1):
           day[i] = day_val[i]
       limiter = ''
       day = limiter.join(day)
       days[Index_num] = day

   elif Index_num == 3:
       day_val = list(day[0:Index_num+1].upper())
       day = list(day)
       for i in range(Index_num+1):
           day[i] = day_val[i]
       limiter = ''
       day = limiter.join(day)
       days[Index_num] = day
   print(days)
   sys.exit()


print(days)

