import os
os.system("cls")

# method
# string list dictionary


#-------------------------- str --------------------------#

# count : 문자열 내에서 특정 문자가 몇 개나 있는지 세어주는 메서드
text = "안녕하세요! hellow! 05!"
count_k = text.count("안")
count_e = text.count("l")
count_n = text.count("5")
print(count_k) # 1 | 한글
print(count_e) # 2 | 영어
print(count_n) # 1 | 숫자

# fimd : 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드 (없을 경우 -1 return)
text = "안녕하세요! hellow! 05!"
position1 = text.find("05")
position2 = text.find("5")
position3 = text.find("6")

print(position1) #15 | 05의 0을 추적
print(position2) #16 | 5을 추적
print(position3) #-1 | 6은 없다!

# index: 문자열 내에서 특정 문자열이 처음 나오는 위치를 찾아주는 메서드 (없을 경우 ValueError)
text = "안녕하세요! hellow! 05!"
try:
    position = text.index("05")
    print(position) #15 | 05의 0을 추적
except ValueError:
    print("그런거 없눈뒈..?")
    
# join: 특정 문자열을 기준으로 다른 문자열들을 합쳐주는 메서드 | split과 반대
alp = ["a","b","c"]
joined_alp = ",".join(alp)
print(joined_alp) # "a,b,c"

# upper: 문자열 내의 모든 소문자를 대문자로 바꾸는 메서드
# lower: 문자열 내의 모든 대문자를 소문자로 바꾸는 메서드
text = "안녕하세요! hellow! 05!"
uppercase_text = text.upper()
print(uppercase_text) # "안녕하세요! HELLOW! 05!"

lovercase_text = text.lower()
print(lovercase_text) # "안녕하세요! hellow! 05!"

# replace: 문자열 내에서 특정 문자열을 다른 문자열로 바꾸는 메서드
text = "안녕하세요! hellow! 05!"
replaced_text = text.replace('05', '영오')
print(replaced_text) # "안녕하세요! hellow! 영오!"

#split: 문자열을 특정 문자를 기준으로 나누는 메서드(결과는 리스트 형태로 반환) | join과 반대
text = "a,b,c"
alp = text.split(",")
print(alp) # ['a', 'b', 'c']


#-------------------------- list --------------------------#

# len: 리스트의 길이를 반환하는 내장 함수
num = [1,2,3,4,5]
name = "영 오"
print(len(num)) # 5 | 리스트원소의 갯수
print(len(name)) # 2 | 문자열의 길이, 띄어쓰기도 카운트

# del: 리스트에서 특정 요소를 삭제하는 연산자
num = [1,2,3,4,5]
del num[3]
print(num) # [1, 2, 3, 5]

# append: 리스트의 맨 뒤에 새로운 요소를 추가하는 메서드
num = [1,2,3,4,5]
num.append(0)
print(num) # [1, 2, 3, 4, 5, 0]

# sort: 리스트를 오름차순으로 정렬하는 메서드
num = [4,5,1,2,3]
num.sort()
print(num) # [1, 2, 3, 4, 5]

# reverse: 리스트의 요소 순서를 반대로 뒤집는 메서드
num = [4,5,1,2,3]
num.reverse()
print(num) # [3, 2, 1, 5, 4] 

# index: 리스트에서 특정 요소의 인덱스를 반환하는 메서드
alp= ['a','b','c']
print(alp.index("b")) #1

# insert: 리스트의 특정 위치에 요소를 삽입하는 메서드
num = [1,2,3,4,5]
num.insert(4,0)
print(num) # [1, 2, 3, 4, 0, 5]

#remove: 리스트에서 특정 요소를 제거하는 메서드
num = [1,2,3,4,5]
num.remove(4)
print(num) # [1, 2, 3, 5]

#pop: 리스트에서 마지막 요소를 빼낸 뒤, 그 요소를 삭제하는 메서드
num = [1,2,3,4,5]
num.pop(3)
print(num) #[1, 2, 3, 5] | 위치를 정하면 해당위치 요소가 pop
num.pop()
print(num) #[1, 2, 3] | 타겟을 정하지 않으면 마지막요소가 pop

#count: 리스트에서 특정 요소의 개수를 세는 메서드
num = [1,2,3,4,5,5,5,4]
print(num.count(5)) #3

#extend: 리스트를 확장하여 새로운 요소들을 추가하는 메서드
num = [1,2,3,4]
num.extend([5,6,7,8])
print(num) # [1, 2, 3, 4, 5, 6, 7, 8]

# += 연산자를 사용해서도 구현할 수도 있다.
num = [1,2,3,4]
num += [5,6,7,8]
print(num) # [1, 2, 3, 4, 5, 6, 7, 8]


#-------------------------- dict --------------------------#

#딕셔너리 초기화
empty_dict = {}

#초기화할 딕셔너리 만들기
my_dict = {"a":1,"b":2,"c":3}
print(my_dict)

# 쌍 추가
my_dict = {"a":1,"b":2,"c":3}
my_dict["d"] = 4
print(my_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# del: 딕셔너리에서 특정 요소를 삭제
my_dict = {"a":1,"b":2,"c":3}
del my_dict["c"]
print(my_dict) # {'a': 1, 'b': 2}

#딕셔너리에서 특정 Key에 해당하는 Value를 얻는 방법 (딕셔너리에 Key가 없는 경우, KeyError)
my_dict = {"a":1,"b":2,"c":3}
print(my_dict["b"]) #2

#keys: 딕셔너리에서 모든 Key를 리스트로 만들기
my_dict = {"a":1,"b":2,"c":3}
key_list = list(my_dict.keys())
print(key_list) # ['a', 'b', 'c']

# values: 딕셔너리에서 모든 Value를 리스트로 만들기
my_dict = {"a":1,"b":2,"c":3}
value_list = list(my_dict.values())
print(value_list) # [1, 2, 3]

# items: 딕셔너리의 모든 키와 값을 튜플 형태의 리스트로 반환
person = {"name":"영오", "age":30, "gender":"male"}
items = person.items()
print(items) #dict_items([('name', '영오'), ('age', 30), ('gender', 'male')])

# clear: 딕셔너리의 모든 요소를 삭제
person = {"name":"영오", "age":30, "gender":"male"}
person.clear()
print(person) # {}

# get: 딕셔너리에서 지정한 키에 대응하는 값을 반환 (딕셔너리에 Key가 없는 경우, None 반환)
person = {"name":"영오", "age":30, "gender":"male"}

name = person.get("name")
print(name) # 영오

email = person.get("email","없엉")
print(email) # 없엉

# in: 해당 키가 딕셔너리 안에 있는지 확인
person = {"name":"영오", "age":30, "gender":"male"}

print("name" in person) # True
print("email" in person) # False