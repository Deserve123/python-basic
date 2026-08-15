# def cal_decorator(fn_name):
#     def fn_inner(*args,**kwargs): 
#         if fn_name.__name__ == 'get_sum':
#             print("正在计算求和...")
#         elif fn_name.__name__ == 'get_qua':
#             print("正在计算求积...")
#         return fn_name(*args,**kwargs)
#     return fn_inner
def logging(flag):
    def cal_decorator(fn_name):
        def fn_inner(*args,**kwargs): 
            if flag == '+':
                print("正在计算求和...")
            elif flag == '*':
                print("正在计算求积...")
            return fn_name(*args,**kwargs)
        return fn_inner
    return cal_decorator

def login_decorator(fn_name):
    def fn_inner(*args,**kwargs):      
        print("校验登录中...")
        return fn_name(*args,**kwargs)
    return fn_inner

@login_decorator
# @cal_decorator
@logging('+')
def get_sum(*args,**kwargs):
    sum=0
    for i in args:
        sum += i    
    for v in kwargs.values():
        sum += v
    return sum   #return sum(args)+sum(kwargs.values())

@login_decorator
# @cal_decorator
@logging('*')
def get_qua(*args,**kwargs):
    sum=1
    for i in args:
        sum *= i    
    for v in kwargs.values():
        sum *= v
    return sum


sum = get_sum(1,2,3,a=4,b=5,c=6)
print(sum)
sum = get_qua(1,2,3,a=4,b=5,c=6)
print(sum)