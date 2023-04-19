import os
os.system("cls")

def my_coroutine():
    while True:
        value = yield
    print('Received value:', value)

# 코루틴 객체 생성
co = my_coroutine()

# 코루틴 실행 준비
next(co)

# 값을 보내기
co.send('Hello, world!')

#=====================================
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen)) # 1
print(next(gen)) # 2
print(next(gen)) # 3
#=====================================
def my_coroutine():
    while True:
        x = yield
        print('Received:', x)

co = my_coroutine()
next(co)

co.send(10) # Received: 10
co.send(20) # Received: 20
co.send(30) # Received: 30

#=====================================

phone_book = {"A":"123-1234", "B":"234-1234","C":"345-1234"}
def search():
    name=yield
    while True:
        if name in phone_book:
            phone_num=phone_book[name]
        else:
            phone_num="그런거몰라!"
        name= yield phone_num
        
        
        
# 코루틴 객체 생성
search_coroutine=search()
next(search_coroutine)

# 검색 예시
result = search_coroutine.send("A")
print(result)
result = search_coroutine.send("a")
print(result)



