#�쳣
try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
else:									#û�д�����ʱ�����Զ�ִ��else���
    print 'no error!'
finally:
    print 'finally...'
print 'END'
##���
try...
except: integer division or modulo by zero
finally...
END

#����
#assert ���� Python������ʱ������ -O �������ر�assert�������� print �����Ļ���
>>> def foo(s):
...     n = int(s)
...     assert n != 0, 'n is zero!'		#����ʧ�����׳��쳣 AssertionError�����'n is zero!'��
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
logging.basicConfig(level=logging.INFO)	#������ָ����¼��Ϣ�ļ�����debug��info��warning��error�ȼ�������
s = '0'
n = int(s)
logging.info('n = %d' % n)				#���һ���ı�������������ļ����ڲ鿴
print 10 / n


#IO���
#��
>>> f = open('/Users/michael/test.txt', 'r')#���ַ��ļ����ļ������ڣ��׳�IOError
>>> f = open('/Users/michael/test.jpg', 'rb')#���������ļ�����Ƶ��ͼƬ��
>>> f.read()							# str �����ʾ
'Hello, world!'
>>> f.close()
##�ı��ļ�
>>> f = open('gbk.txt', 'rb')			
>>> u = f.read().decode('gbk')			#���ı��ļ���GBK������ļ����ֶ�ת��
>>> u
u'\u6d4b\u8bd5'							#unicode
>>> print u
����
##�Զ�ת��
import codecs
with codecs.open('...', 'r', 'gbk') as f:
    f.read() # u'\u6d4b\u8bd5'
	

#with
with open('/path/to/file', 'r') as f:	#����ļ������ڣ����޷��رգ������� with ���൱��try...  finally...
    print f.read()
	
#read(size)�������ļ�  �� readline ÿһ�ζ�һ��  �� readlins  һ�ζ�ȡ�������ݲ����з���list ���ʺ϶������ļ���
for line in f.readlines():
    print(line.strip()) 				# ��ĩβ��'\n'ɾ��
	
#д
>>> f = open('...', 'w')				#��ʶ��'w'����'wb'��ʾд�ı��ļ���д�������ļ�
>>> f.write('Hello, world!')
>>> f.close()							#ʹ�ı�д�����
##�� with �����ļ���ʧ
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')

#�����ļ���Ŀ¼
# �鿴��ǰĿ¼�ľ���·��:
>>> os.path.abspath('.')
'/Users/michael'
# ��ĳ��Ŀ¼�´���һ����Ŀ¼��
# ���Ȱ���Ŀ¼������·����ʾ����:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# Ȼ�󴴽�һ��Ŀ¼:
>>> os.mkdir('/Users/michael/testdir')
# ɾ��һ��Ŀ¼:
>>> os.rmdir('/Users/michael/testdir')
# ���ļ�������:
>>> os.rename('test.txt', 'test.py')
# ɾ���ļ�:
>>> os.remove('test.py')
#�г���ǰĿ¼�µ�����Ŀ¼
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Adlm', 'Applications', 'Desktop', ...]
#�г����е�.py�ļ�
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']

#���л� ���ѱ������ڴ��б�ɿɴ洢����Ĺ��̳�֮Ϊ���л���
#cPickle��pickle ��ʽ
>>> try:
>>>     import cPickle as pickle
>>> except ImportError:
>>>     import pickle
>>> d = dict(name='Bob', age=20, score=88)
>>> pickle.dumps(d)						#���л�
"(dp0\nS'age'\np1\nI20\nsS'score'\np2\nI88\nsS'name'\np3\nS'Bob'\np4\ns."
>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)					#�����ļ�
>>> f.close()
>>> f = open('dump.txt', 'rb')
>>> d = pickle.load(f)					#�����л�
>>> f.close()
>>> d
{'age': 20, 'score': 88, 'name': 'Bob'}

#JSON ��ʽ����׼��ʽ���죩
>>> import json
>>> d = dict(name='Bob', age=20, score=88)
>>> json.dumps(d)						#���л�
'{"age": 20, "score": 88, "name": "Bob"}'#json��ʽ

>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'#json��ʽ
>>> json.loads(json_str)				#�����л�
{u'age': 20, u'score': 88, u'name': u'Bob'}

#JSON ���ף����л�class��
json.dumps(s, default=lambda obj: obj.__dict__)#ͨ��class��ʵ������һ��__dict__���ԣ�������һ��dict

def dictstudent(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dictstudent))  #�����л�


#����
#fork() ���η��أ������̴η��ؽ���ID ���ӽ��̷��� 0  ���������� win��
import os
print 'Process (%s) start...' % os.getpid()#��ý��̵�ID
pid = os.fork()							#�������������������
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())#�ֱ��������̵�ID �͸�����ID
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
	
#���
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.

#multiprocessing ��winϵͳ��
from multiprocessing import Process
import os
## �ӽ���Ҫִ�еĴ���
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
##�����ӽ���ʱ��ֻ��Ҫ����һ��ִ�к����ͺ����Ĳ���
if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = multiprocessing.Process(target=run_proc, args=('test',))#�����ӽ���
    print 'Process will start.'
    p.start()							#����
    p.join()							#join()�������Եȴ��ӽ��̽������ټ����������У�ͨ�����ڽ��̼��ͬ��
    print 'Process end.'

#Pool ���̳�
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
    p = Pool()							#��Ĭ��������һ��һ��ִ��
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))#Ԥ���趨����
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
	
#���̼�ͨ��
from multiprocessing import Process, Queue
import os, time, random

##д���ݽ���ִ�еĴ���:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

##�����ݽ���ִ�еĴ���:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # �����̴���Queue�������������ӽ��̣�
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # �����ӽ���pw��д��:
    pw.start()
    # �����ӽ���pr����ȡ:
    pr.start()
    # �ȴ�pw����:
    pw.join()
    # pr����������ѭ�����޷��ȴ��������ֻ��ǿ����ֹ:
    pr.terminate()
	
#�߳� ������������ɶ������ɣ�Ҳ������һ�������ڵĶ��߳���ɡ���
import time, threading

##�ٶ�����������д��:
balance = 0

def change_it(n):
    # �ȴ��ȡ�����Ӧ��Ϊ0:
    global balance
    balance = balance + n
    balance = balance - n
	
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # ��Ҫ��ȡ��:
        lock.acquire()					#����߳�֮�������໥���ŵģ�����һ���߳̽���ʱҪ����
        try:
            # ���ĵظİ�:
            change_it(n)
        finally:
            # ������һ��Ҫ�ͷ���:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

#ThreadLocal ���󣬲�ʹ��ȫ�ֱ���ʱ�������߳�֮��ĸ��ţ����㴫��
import threading

##����ȫ��ThreadLocal����:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    # ��ThreadLocal��student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
##���
Hello, Alice (in Thread-A)
Hello, Bob (in Thread-B)

