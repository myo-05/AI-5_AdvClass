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
    result = [1]
    if n == 1:
        return [1]
    elif n == 2:
        return [1 , 1]
    elif n > 2:
        for i in range(len(pt(n-1))-1):
            result.append(pt(n-1)[i]+pt(n-1)[i+1])
        result.append(1)
        return result
    else:
        return print("[자연수를 입력하세요]")
        
print(pt(1))
print(pt(2))
print(pt(3))
print(pt(4))
print(pt(5))
print(pt(6))
print(pt(7))
print(pt(8))
