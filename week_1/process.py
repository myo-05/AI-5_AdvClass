from multiprocessing import Process
import os
# os.system("cls")

# [참고] 매 실행마다 PID는 재할당 받기에 실행마다 다른 PID가 출력되는 것이 정상이다! 
# [참고] 또한 os.getpid는 시스템의 PID를 가져오는 것임으로 아래 두 경우 모두 parent PID는 동일하다 


# ============1. 동일한 작업을 하는 프로세스 생성=============

def foo():
    print('child process:', os.getpid())  # 자식프로세스의 PID값
    print('my parent is:', os.getppid())  # 부모프로세스의 PID값

# 자식프로세스는 얼마든지 생성 가능
if __name__ == '__main__':  # 현재 모듈(__name__)이 직접실행(__main__)될 때 조건문을 실행해
    print('parent same_process:', os.getpid())
    child1 = Process(target=foo).start()  # foo()를 실행하는 프로세스(child1~3)를 만들어서 실행해
    child2 = Process(target=foo).start()
    child3 = Process(target=foo).start()

'''결과
parent same_process: 45652
child process: 21772
child process: 4932
child process: 31768
my parent is: 45652
my parent is: 45652
my parent is: 45652
'''

# 시각적으로 실행 순서를 보기 위한 구분선
print("="*30)
'''
구분선이 여러개 생기는 것으로 보아
child process들은 각기 다른 process 과정임을 알 수 있고, 시스템 콜이 반복되어 자원이 낭비됨을 볼 수 있다.
구분선의 위치가 매 실행마다 바뀌는 것으로 보아
매실행마다 프로세스들의 실행속도 차이가 존재함을 알 수 있다.
'''



# ============2. 각기 다른 작업을 하는 프로세스 생성=============

def bar():
    print('This is bar:', os.getpids())

def baz():
    print('This is baz:', os.getpid())
    
def qux():
    print('This is qux:', os.getpid())


# 각기 다른 작업의 자식프로세스
if __name__ == '__main__':
    print('parent diff_process:', os.getpid()) 
    child4 = Process(target=bar).start()  
    child5 = Process(target=baz).start() 
    child6 = Process(target=qux).start()  

'''결과
parent diff_process: 45652
This is bar: 21780
This is baz: 31192
This is qux: 21388
'''

'''프로세스 테스트
의도적으로 bar()에 오타를 주어 error를 발생시켰을 때,
child4 가 error를 일으키며 프로세스가 도중에 멈춘다.
이는 process가 하나의 실행흐름을 갖기 때문이다.
'''