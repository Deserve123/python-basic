import threading

global_num = 0
mutex = threading.Lock()

def get_sum1():
    mutex.acquire()
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'线程1的资源抢占:{global_num}')
    mutex.release()

def get_sum2():
    mutex.acquire()
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'线程2的资源抢占:{global_num}')
    mutex.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=get_sum1)
    t2 = threading.Thread(target=get_sum2)

    t1.start()
    t2.start()