# 多线程
import threading
import random, time, queue
from multiprocessing.managers import BaseManager

# 新线程执行的代码:
# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n += 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()  # 等待子线程执行完成后，才会继续向下执行
# print('thread %s ended.' % threading.current_thread().name)


# 假定这是你的银行存款:
# balance = 5
# lock = threading.Lock()
#
#
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance += n
#     balance -= n
#
#
# def run_thread(n):
#     # 线程锁保证函数每次进去都只有一个线程
#     for i in range(100000):
#         lock.acquire()  # 先要获取锁:
#         try:
#             change_it(n)
#         except Exception as e:
#             print('error', e.args.__str__())
#         finally:
#             lock.release()  # 改完了一定要释放锁:
#
#
# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。
# 你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，
# 也不用管理锁的问题，ThreadLocal内部会处理。
# 创建全局ThreadLocal对象:
# local_thread = threading.local()
#
# def process_student():
#     # 获取当前线程关联的student:
#     std = local_thread.student
#     print('Hello,%s (in %s)' % (std, threading.current_thread().name))
#
#
# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_thread.student = name
#     process_student()
#
#
# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread_A')
# t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread_B')
# t1.start()
# t2.start()
# t1.join()
# t2.join



