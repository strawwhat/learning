#/usr/bin/env python
# *-*coding:utf-8 *-*

q = [3,6,9]
t = [2,5,8]
q1 = [2,4,6,8,10]
t1 = [1,3,5,7,9]

def race(qi, tian):
	race_result = []
	for i in range(len(qi)):
		if i == 0:
			race_result.append((qi.pop(), tian.pop(i)))
		else:
			race_result.append((qi.pop(), tian.pop()))
	print(race_result)

race(q, t)
race(q1, t1)
