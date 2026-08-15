import multiprocessing
import time
import os

def coding(name,num):
    for i in range(1,num):
        time.sleep(0.1)
        print(f"{name}第{i}次编码")
    print(f'进程1的pid: {os.getpid()},{multiprocessing.current_process()},父进程的ppid:{os.getppid()}')


def music(name,num):
    for i in range(1,num):
        time.sleep(0.1)
        print(f"{name}第{i}次听音乐")   # '\n'可能会抢资源
    print(f'进程2的pid: {os.getpid()},{multiprocessing.current_process()},父进程的ppid:{os.getppid()}')
    
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=coding,args=('哈哈',6))
    p2 = multiprocessing.Process(target=music,kwargs={'num':6,'name':'嘻嘻'})

    p1.start()
    p2.start()

    print(f'main进程的pid: {os.getpid()},{multiprocessing.current_process()},父进程的ppid:{os.getppid()}')
    