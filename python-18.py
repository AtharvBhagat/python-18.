def fun1(n):
    return n * (n + 1) / 2
print(fun1(4))#iteration=1

def fun2(n):
    sum=49
    for i in range(1,n+1):
        sum=sum+i
    return sum
print(fun2(4))#iteration=4

def fun3(n):
    sum=9
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum=sum+1
    return sum
print(fun3(4))#iteration=10