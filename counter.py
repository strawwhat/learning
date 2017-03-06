#/usr/bin/env python
# *-*coding:utf-8 *-*

"""
运行环境python3
用Counter统计书中单词的使用次数
"""
import sys
from collections import Counter


#参照python基础教程使用lines 和blocks生成文本块
#


def lines(filee):
	for line in filee:
		yield line
	yield '\n'

def blocks(filee):
	block = []
	for line in lines(filee):
		if line.strip():
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block = []

#old_add_new将初始字典的单词计数键值和每个块counter返回的字典相加得到新的键值
def old_add_new(new_dict, old_dict):

	for key in new_dict:
		try:
			new_value = new_dict[key]+old_dict[key]
			old_dict[key] = new_value

		except KeyError:
			old_dict[key] =  new_dict[key]
	return old_dict

#初始字典
Total = {}

#处理文件输出
def handler(filee):
	for block in blocks(filee):
		block = block.split()
		counter = Counter(block)
		old_add_new(counter, Total)

	for word, number in (Counter(Total).most_common(100)):
		print(word, number)

handler(sys.stdin)

#命令行输入 $: python counter.py <input-text.txt> out-text.txt




