def fibonacci(n):
    n = eval(input("enter a whole integer"))
    if n<0:
        print ("integer cannot be less than zero")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    