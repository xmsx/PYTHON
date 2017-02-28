# -*- coding: utf-8 -*-
#数据类型
print 123       				#整数 int
print 1.23e3    				#浮点数 float
print 0xff00 					#16进制
print 'MFS'+"mfs"				#字符串
print 'Bob said \"I\'m OK\".'
print 1==2						#布尔值 False

#字符串
# print 字符之间可以用 ',' 或 '+' 连接，但是 ',' 表示一个空格
print 'Bob said \"I\'m OK\".'									#字符串中的反斜杠 '\' 转义特殊字符
print r'''"To be, or not to be": that is the question.
Whether it's nobler in the mind to suffer.'''					#字符串中 Raw 字符串 中的特殊字符不用转义 '''...''' 用来打印多行字符串
print u'中文' 													#打印中文要在字符串前加'u'

#布尔值 not and or 
# 'and' , 'or' 采取短路计算，按顺序运算，由谁决定 T or F 输出谁
>>> print 1 or 2
1
>>> print 0 and 2
0
>>> print 0 or 2
2 

#变量定义
x1 = 1							#因为是动态编程，变量的类型是可以随意转化的，不必声明变量的类型
d = 3
n = 100
x100 = x1+d*(n-1)
s = (x100+x1)*n/2
print s

#list
>>> L = ['Adam',95.5,'Lisa',85,'Bart',59,[1,2,3]]				#因为是动态编程，L 中每一个值是随意的
>>> print L
['Adam', 95.5, 'Lisa', 85, 'Bart', 59, [1, 2, 3]]

>>> L=[1,3,5]													#索引有负值，代表从后向前
>>> print L[0],L[1],L[2]
1 3 5
>>> print L[-1],L[-2],L[-3]
5 3 1

L.append(7)						#将 7 添加在list尾部
L.insert(2，7)					#将 7 添加在索引为 2 的位置，其余元素后移
L.pop(2)						#弹出索引为 2 的元素，并返回这个元素

#tuple
t = ('Adam',)					#一个元素要多写 ','
t = ('a', 'b', ['A', 'B']) 		#tuple 是不可改变的，但是如果tuple中放了 list，则其中的 list 可变

#条件判断和循环
#if
score = 85
if score>=90:
    print 'excellent'
elif score>=80:
    print 'good'
elif score>=60:
    print 'passed'
else:
    print 'failed'

#for
L = [75, 92, 59, 68]
sum = 0.0
for s in L:
    sum = sum+s
print sum / 4

#while break
sum = 0
x = 1
n = 1
while True:
    if n==21:
        break
    sum+=x
    x*=2
    n+=1
print sum

#dict （类似 C 的 map）
#遍历dict
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for k in d:
    print k,':',d[k]

#set （去重，无序，内部元素不可变）
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
x = 'MFS'
if x in weekdays:
    print 'input ok'
else:
    print 'input error'
	
#更新
weekdays.add('MFS')
weekdays.remove('MFS')

#1. 有序集合：list，tuple，str和unicode；
#2. 无序集合：set
#3. 无序集合并且具有 key-value 对：dict

#函数
def average(*args):				#可变参数的名字前面有个 * 号，可以传入0个、1个或多个参数给可变参数
    if not args:
        return 0.0
    else:
        return sum(args)*1.0/len(args)

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)

#切片
>>> L = range(1,100)
>>> print L[1:10]				#从索引 1 - 9
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print L[2:10:3]				#从索引 2 - 10 ，没隔三个取一个
[3, 6, 9]

# enumerate() 函数
L = ['Adam', 'Lisa', 'Bart', 'Paul']
enumerate(L) = [(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]

#values 和 itervalues
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
d.values() = [85, 95, 59]		#itervalues 与 values 作用相同但是节省内存

#items 和 iteritems
>>> d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
>>> print d.items()
[('Lisa', 85), ('Adam', 95), ('Bart', 59)]

#zip
print [x*y for x,y in zip(range(1,100,2),range(2,101,2))]		#生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print [x*100+y*10+z for x in range(1,10) for y in range(0,10) for z in range (1,10) if x==z]				#利用 3 层for循环的列表生成式，找出对称的 3 位数对称数。

