#/usr/bin/env python
# *-*coding:utf-8 *-*
 
#运行环境python 3.5.2
#选出回文数字

def Palindrome(n):
	for i in range(800000, 10000000):
		number = list(str(i))
		#使用reversed把列表进行反向迭代， eval求值连接后的字符串
		if number == list(reversed(number)) and eval('+'.join(number)) == n:
			print(i)

Palindrome(52)

