def fib_num(n):
    if n>=1 and n<=2 :
        return 1
    elif n>2 :
        return fib_num(n-1)+fib_num(n-2)

if __name__ == '__main__':
    number = fib_num(5)
    print(number)

