#/usr/bin/env python
# *-*coding:utf-8 *-*

"""
把书中单词数据制作成pdf
"""
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import *
from reportlab.lib import colors


#对象容器
elements = []
#列表样式
styles = getSampleStyleSheet()
#设置文件标题
doc_title = SimpleDocTemplate('Words Times')
#添加表格的标题文字， 风格为Title
elements.append(Paragraph('Number of times the word appears in the book', styles['Title']))

#创建二维数据表格
filepath = '~/janeoutput.txt'
data = [['BookName', 'Jane Eyre']]
with open(filepath) as files:
	for line in files:
		data.append(line.split())

	data.append(['End!', 'End!'])
#print(data)

#设置表格风格 字体对齐方式 网格以及划线

ts = [('ALIGN', (1,1), (-1,-1), 'CENTER'),
      ('LINEABOVE', (0,0), (-1,0), 1, colors.yellow),
      ('LINEBELOW', (0,0), (-1,0), 1, colors.green),
      ('FONT', (0,0), (-1,0), 'Times-Bold'),
#下三行设置
	 ('LINEABOVE', (0,-1), (-1,-1), 1, colors.blue),
     ('LINEBELOW', (0,-1), (-1,-1), 0.5, colors.black, 1, None, None, 4,1),
     ('LINEBELOW', (0,-1), (-1,-1), 1, colors.black),
     ('FONT', (0,-1), (-1,-1), 'Times-Bold')]

#将数据和风格添加到Table中创建Table对象， 将Table对象加入到elements中
table = Table(data, style= ts)
elements.append(table)
#创建图像
doc_title.build(elements)
		
		
		
		
		
		
		
