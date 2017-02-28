#异常
try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
else:									#没有错误发生时，会自动执行else语句
    print 'no error!'
finally:
    print 'finally...'
print 'END'
##输出
try...
except: integer division or modulo by zero
finally...
END

#调试
#assert 断言 Python解释器时可以用 -O 参数来关闭assert，避免了 print 产生的混乱
>>> def foo(s):
...     n = int(s)
...     assert n != 0, 'n is zero!'		#断言失败则抛出异常 AssertionError，输出'n is zero!'，
...     return 10 / n
...
>>> def main():
...     foo('0')
...
>>> main()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in main
  File "<stdin>", line 3, in foo
AssertionError: n is zero!

#logging
import logging
logging.basicConfig(level=logging.INFO)	#允许你指定记录信息的级别，有debug，info，warning，error等几个级别
s = '0'
n = int(s)
logging.info('n = %d' % n)				#输出一段文本，可以输出到文件便于查看
print 10 / n


#IO编程
#读
>>> f = open('/Users/michael/test.txt', 'r')#读字符文件，文件不存在，抛出IOError
>>> f = open('/Users/michael/test.jpg', 'rb')#读二进制文件（视频，图片）
>>> f.read()							# str 对象表示
'Hello, world!'
>>> f.close()
##文本文件
>>> f = open('gbk.txt', 'rb')			
>>> u = f.read().decode('gbk')			#读文本文件（GBK编码的文件）手动转化
>>> u
u'\u6d4b\u8bd5'							#unicode
>>> print u
测试
##自动转化
import codecs
with codecs.open('...', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'
	

#with
with open('/path/to/file', 'r') as f:	#如果文件不存在，则无法关闭，所以用 with ，相当于try...  finally...
    print f.read()
	
#read(size)按量打开文件  ； readline 每一次读一行  ； readlins  一次读取所有内容并按行返回list （适合读配置文件）
for line in f.readlines():
    print(line.strip()) 				# 把末尾的'\n'删掉
	
#写
>>> f = open('...', 'w')				#标识符'w'或者'wb'表示写文本文件或写二进制文件
>>> f.write('Hello, world!')
>>> f.close()							#使文本写入磁盘
##用 with 避免文件丢失
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')

#操作文件和目录
# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')
# 对文件重命名:
>>> os.rename('test.txt', 'test.py')
# 删掉文件:
>>> os.remove('test.py')
#列出当前目录下的所有目录
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Adlm', 'Applications', 'Desktop', ...]
#列出所有的.py文件
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']

#序列化 （把变量从内存中变成可存储或传输的过程称之为序列化）
#cPickle和pickle 格式
>>> try:
>>>     import cPickle as pickle
>>> except ImportError:
>>>     import pickle
>>> d = dict(name='Bob', age=20, score=88)
>>> pickle.dumps(d)						#序列化
"(dp0\nS'age'\np1\nI20\nsS'score'\np2\nI88\nsS'name'\np3\nS'Bob'\np4\ns."
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)					#存入文件
>>> f.close()
>>> f = open('dump.txt', 'rb')
>>> d = pickle.load(f)					#反序列化
>>> f.close()
>>> d
{'age': 20, 'score': 88, 'name': 'Bob'}

#JSON 格式（标准格式，快）
>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)						#序列化
'{"age": 20, "score": 88, "name": "Bob"}'#json格式

>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'#json格式
>>> json.loads(json_str)				#反序列化
{u'age': 20, u'score': 88, u'name': u'Bob'}

#JSON 进阶（序列化class）
json.dumps(s, default=lambda obj: obj.__dict__)#通常class的实例都有一个__dict__属性，它就是一个dict

def dictstudent(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dictstudent))  #反序列化


#进程
#fork() 两次返回，父进程次返回进程ID ，子进程返回 0  （不适用于 win）
import os
print 'Process (%s) start...' % os.getpid()#获得进程的ID
pid = os.fork()							#返回两次所以输出两次
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())#分别获自身进程的ID 和父进程ID
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
	
#输出
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.

#multiprocessing （win系统）
from multiprocessing import Process
import os
## 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
##创建子进程时，只需要传入一个执行函数和函数的参数
if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = multiprocessing.Process(target=run_proc, args=('test',))#创建子进程
    print 'Process will start.'
    p.start()							#启动
    p.join()							#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print 'Process end.'

#Pool 进程池
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()							#有默认批量，一批一批执行
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))#预先设定进程
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
	
#进程间通信
from multiprocessing import Process, Queue
import os, time, random

##写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

##读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
	
#线程 （多任务可以由多进程完成，也可以由一个进程内的多线程完成。）
import time, threading

##假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n
	
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()					#多个线程之间是有相互干扰的，所以一个线程进行时要上锁
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

#ThreadLocal 对象，不使用全局变量时，避免线程之间的干扰，方便传递
import threading

##创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
##输出
Hello, Alice (in Thread-A)
Hello, Bob (in Thread-B)

