import os
os.system("cls")

# 파스칼 삼각형 만들기!
'''
pt(1) = [ 1 ] 
pt(2) = [ 0+pt(1)[0], pt(1)[0]+0 ]
pt(3) = [ 0+pt(2)[0], pt(2)[0]+pt(2)[1] ,pt(2)[1]+0 ]
pt(4) = [ 0+pt(3)[0], pt(3)[0]+pt(3)[1], pt(3)[1]+pt(3)[2] ,pt(3)[2]+0 ]
...
pt(n) = [ 0+pt(n-1)[0], pt(n-1)[0]+pt(n-1)[1], ... , pt(n-1)[n-3]+pt(n-1)[n-2], pt(n-1)[n-2]+0 ] 
...

'''
def pt(n):
    
    pt(n)[0] == pt(n-1)[0]
    pt(n)[n-1] == pt(n-1)[n-2]
    result=[]
    for _ in range(1,n+1):
        if n == 1:
            return [n]
        elif n >= 2:
            result.append()
            return result
        else:
            return print("[자연수를 입력하세요] 아, 그거 그렇게 하는거 아닌뒈~")
# pt(n)의 인덱스는 pt(n-1)의 인덱스 2개를 더해서 만드는 값이다.
# 그러니깐 pt(n-1)의 인덱스를 빼와서 계산한 다음 pt(n)의 new 인덱스에 첨부하는 식으로? 해야 하나
        
    
print(pt(10))
