# -*- coding: utf-8 -*-
#高阶函数 ：因为函数能作为一个变量，所以函数中的参数可以是函数，也可以返回函数。
#map
def f(x):					
    return x*x
#将map() 接受 f 函数 和 list 生成一个新的list 
map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])==[1, 4, 9, 10, 25, 36, 49, 64, 81]

def format_name(s):
    return s.title()		#title() 将字符串首字母大写其余小写
map(format_name, ['adam', 'LISA', 'barT'])

#reduce
def f(x, y):
    return x+y
#类似 map() 但是，f必须接受两个参数,初始值为100，实现
#先计算初始值和头元素：f(100, 1)，结果为101；
#计算头两个元素：f(101, 3)，结果为104；
#再把结果和第3个元素计算：f(4, 5)，结果为109；
reduce(f, [1, 3, 5],100)

#filter
import math
def is_sqr(x):
    return x and math.sqrt(x)-int(math.sqrt(x))==0
#filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
print filter(is_sqr, range(1, 101))

#sorted
def cmp_ignore_case(s1, s2):#如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
    if s1.lower()>s2.lower():
        return 1
    return -1
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

#返回函数
def calc_prod(lst):
    def prod(x, y):
        return x*y
    def f():
        return reduce(prod,lst)
    return f
f = calc_prod([1, 2, 3, 4])

#闭包 ：内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
def count():
    fs = []
    for i in range(1, 4):
        def r(m=i):
            return m*m
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

#匿名函数 lambda  （只能有一个表达式，不写return）
lambda x: x*x

#装饰器   （接收一个函数作为参数，然后，返回一个新函数。@ 语法）
import time
def performance(f):   		#装饰器函数
    print "call ",f.__name__,"() in",time.ctime()
    return f
@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
#输出
#call  factorial () in Tue Feb  7 15:49:02 2017
#3628800

import time

def performance(unit): 		#带参数的装饰器函数（双层函数）
    def g(f):
        print 'call',f.__name__,'() in '+time.ctime(),unit
        return f
    return g
@performance('s')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

import time, functools
#
def performance(unit):
    def g(f):
        @functools.wraps(f)	#修饰，作用使原函数只使用装饰器的功能
        def fn():
            print 'call',f.__name__,'() in '+time.ctime(),unit
            return f
        return fn
    return g
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial.__name__

#偏函数
>>> def int2(x, base=2):
>>>     return int(x, base)
>>> int2('1000000')
64
>>> int2('1010101')
85

>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85

import functools
def cmp_ignore_case(s1, s2):
    if s1.lower()>s2.lower():
        return 1
    return -1
sorted_ignore_case = functools.partial(sorted,cmp=cmp_ignore_case)

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

#模块的导入
try:
    from cStringIO import StringIO						#优先导入计算速度快的  cStringIO
except ImportError:
    from StringIO import StringIO

>>> from __future__ import division						#使用新版本的功能 ，导入模块 __future__
>>> print 10 / 3
3.3333333333333335

#类
class Person(object):
	__slots__ = ('name', '_gender', '__score', 'birth' ,'job') # 用tuple定义允许绑定的属性名称
    def __init__(self, name, gender, score, birth,**kw):   #**kw是关键字参数，用于字典 
        self.name = name
        self._gender = gender							#可以在子类中使用
		self.__score = score							#私有属性，不可以在子类中使用
        self.birth = birth
        for k,v in kw.items():						#items()用于字典kw的遍历
            setattr(self, k, v)						#setattr(self, k, v)就等价于self.k = v

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

# @property 装饰器就是负责把一个方法变成属性调用
class Person(object):
    def __init__(self, name, score):
        self.name=name
        self.__score=score
    @property
    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade
print p2.get_grade
print p3.get_grade

# @classmethod ，将方法将绑定到 Person 类上
class Person(object):
    __count = 0				#属于类属型
    def __init__(self ,name):
        self.name=name
        Person.__count +=1
    @classmethod			#属于类方法
    def how_many(cls):
        return cls.__count

print Person.how_many()		#输出0
p1 = Person('Bob')
print Person.how_many()		#输出1

#继承
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)		#初始化父类
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
#isinstance() 判断类型是否相同
print isinstance(t, Person)	#True
print isinstance(t, Student)#False
print isinstance(t, Teacher)#True
print isinstance(t,object)	#True

#定制类
class Fib(object):
    def __init__(self):
        pass
	def __cmp__(self, s):	#定制排序
		pass
    def __str__(self):		#定制打印类型
        return str(self.x)
    def __len__(self): 		#定制长度
        return len(self.x)
    def __call__(self,num):	#定制呼叫
        L=[0,1]
        for i in range(num-2):
            L.append(L[-1]+L[-2])
        self.x=L
        return self.x
f = Fib()
print f(10)					#调用 __call__ 方法