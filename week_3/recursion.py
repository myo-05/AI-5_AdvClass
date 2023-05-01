import sys
import os
os.system("cls")

#리턴값 無 재귀함수

#리턴값 有 재귀함수


#### 종료조건이 명시되지 않을 경우 ####
def rucursion(n):
    print(n)
    rucursion(n+1)
    
# rucursion(1)

# 에러발생 RecursionError: maximum recursion depth exceeded while calling a Python object
# 종료조건이 명시되지 않을 경우 생기는 에러! 

# 최대 재귀 깊이(maximum recursion depth): 재귀함수를 최대로 할 수 있는 횟수
# print(sys.getrecursionlimit())

# 재귀로 풀어보기(1) 팩토리얼
def factorial(n):
    if n <= 1 :
        return 1
    return n * factorial(n-1)

# print(factorial(16))

# 재귀로 풀어보기(2) 피보나치
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(10))
