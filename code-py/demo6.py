for i in range(1,6):
    print(i)
print('-'*27)

class my_iterator:
    # 初始化 再重写两个方法
    def __init__(self,start,end):
       self.current = start
       self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration #停止并抛出异常
        self.value = self.current
        self.current += 1
        return self.value

for i in my_iterator(1,6):
    print(i)

my_itr = my_iterator(10,12)
print(next(my_itr))
print(next(my_itr))
print(next(my_itr)) #抛出异常