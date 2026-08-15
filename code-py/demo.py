# def fn_outer(num1):
#     def fn_inner(num2):
#         sum=num1+num2
#         print(f"{sum}")     
#     return fn_inner

def fn_outer():
    a=100
    def fn_inner():
        nonlocal a
        a=a+1
        print(f'{a}')
    return fn_inner



def cal_decorator(fn_name):
    def cal_inner(x,y):
        print("正在计算...")
        return fn_name(x,y)
    return cal_inner    

@cal_decorator #cal = cal_decorator(cal)
def cal(x,y): 
    return x+y

if __name__ == '__main__':
    fn_inner = fn_outer()
    fn_inner()
    fn_inner()

    cal = cal_decorator(cal)
    print(cal(10,20))

