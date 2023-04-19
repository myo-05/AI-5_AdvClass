import os
os.system("cls")

phone_book = {"A":"123-1234", "B":"234-1234","C":"345-1234"}
def search():
    name=yield
    while True:
        if name in phone_book:
            phone_num=phone_book[name]
        else:
            phone_num="그런 사람 없는데유?!"
        name= yield phone_num
        
        
        
# 코루틴 객체 생성
search_coroutine=search() #코루틴 객체생성
next(search_coroutine) #코루틴 실행준비

# 검색 예시
result = search_coroutine.send("A") # yield = A
print(result) # 123-1234
result = search_coroutine.send("a") # yield = a
print(result) # 그런 사람 없는데유?!
result = search_coroutine.send("B") # yield = B
print(result) # 234-1234
result = search_coroutine.send("C") # yield = C
print(result) # 345-1234



