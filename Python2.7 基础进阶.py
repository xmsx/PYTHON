# -*- coding: utf-8 -*-
#�߽׺��� ����Ϊ��������Ϊһ�����������Ժ����еĲ��������Ǻ�����Ҳ���Է��غ�����
#map
def f(x):					
    return x*x
#��map() ���� f ���� �� list ����һ���µ�list 
map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])==[1, 4, 9, 10, 25, 36, 49, 64, 81]

def format_name(s):
    return s.title()		#title() ���ַ�������ĸ��д����Сд
map(format_name, ['adam', 'LISA', 'barT'])

#reduce
def f(x, y):
    return x+y
#���� map() ���ǣ�f���������������,��ʼֵΪ100��ʵ��
#�ȼ����ʼֵ��ͷԪ�أ�f(100, 1)�����Ϊ101��
#����ͷ����Ԫ�أ�f(101, 3)�����Ϊ104��
#�ٰѽ���͵�3��Ԫ�ؼ��㣺f(4, 5)�����Ϊ109��
reduce(f, [1, 3, 5],100)

#filter
import math
def is_sqr(x):
    return x and math.sqrt(x)-int(math.sqrt(x))==0
#filter()�����жϽ���Զ����˵�������������Ԫ�أ������ɷ�������Ԫ����ɵ���list��
print filter(is_sqr, range(1, 101))

#sorted
def cmp_ignore_case(s1, s2):#��� x Ӧ������ y ��ǰ�棬���� -1����� x Ӧ������ y �ĺ��棬���� 1����� x �� y ��ȣ����� 0��
    if s1.lower()>s2.lower():
        return 1
    return -1
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

#���غ���
def calc_prod(lst):
    def prod(x, y):
        return x*y
    def f():
        return reduce(prod,lst)
    return f
f = calc_prod([1, 2, 3, 4])

#�հ� ���ڲ㺯����������㺯���ı���������Ҳ���������Ȼ�󷵻��ڲ㺯�����������Ϊ�հ���Closure����
def count():
    fs = []
    for i in range(1, 4):
        def r(m=i):
            return m*m
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

#�������� lambda  ��ֻ����һ�����ʽ����дreturn��
lambda x: x*x

#װ����   ������һ��������Ϊ������Ȼ�󣬷���һ���º�����@ �﷨��
import time
def performance(f):   		#װ��������
    print "call ",f.__name__,"() in",time.ctime()
    return f
@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
#���
#call  factorial () in Tue Feb  7 15:49:02 2017
#3628800

import time

def performance(unit): 		#��������װ����������˫�㺯����
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
        @functools.wraps(f)	#���Σ�����ʹԭ����ֻʹ��װ�����Ĺ���
        def fn():
            print 'call',f.__name__,'() in '+time.ctime(),unit
            return f
        return fn
    return g
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial.__name__

#ƫ����
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

#ģ��ĵ���
try:
    from cStringIO import StringIO						#���ȵ�������ٶȿ��  cStringIO
except ImportError:
    from StringIO import StringIO

>>> from __future__ import division						#ʹ���°汾�Ĺ��� ������ģ�� __future__
>>> print 10 / 3
3.3333333333333335

#��
class Person(object):
	__slots__ = ('name', '_gender', '__score', 'birth' ,'job') # ��tuple��������󶨵���������
    def __init__(self, name, gender, score, birth,**kw):   #**kw�ǹؼ��ֲ����������ֵ� 
        self.name = name
        self._gender = gender							#������������ʹ��
		self.__score = score							#˽�����ԣ���������������ʹ��
        self.birth = birth
        for k,v in kw.items():						#items()�����ֵ�kw�ı���
            setattr(self, k, v)						#setattr(self, k, v)�͵ȼ���self.k = v

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

# @property װ�������Ǹ����һ������������Ե���
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

# @classmethod �����������󶨵� Person ����
class Person(object):
    __count = 0				#����������
    def __init__(self ,name):
        self.name=name
        Person.__count +=1
    @classmethod			#�����෽��
    def how_many(cls):
        return cls.__count

print Person.how_many()		#���0
p1 = Person('Bob')
print Person.how_many()		#���1

#�̳�
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)		#��ʼ������
        self.score = score

class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
#isinstance() �ж������Ƿ���ͬ
print isinstance(t, Person)	#True
print isinstance(t, Student)#False
print isinstance(t, Teacher)#True
print isinstance(t,object)	#True

#������
class Fib(object):
    def __init__(self):
        pass
	def __cmp__(self, s):	#��������
		pass
    def __str__(self):		#���ƴ�ӡ����
        return str(self.x)
    def __len__(self): 		#���Ƴ���
        return len(self.x)
    def __call__(self,num):	#���ƺ���
        L=[0,1]
        for i in range(num-2):
            L.append(L[-1]+L[-2])
        self.x=L
        return self.x
f = Fib()
print f(10)					#���� __call__ ����