import threading
import os
os.system("cls")

# [참고] 매 실행마다 PID는 재할당 받기에 실행마다 다른 PID가 출력되는 것이 정상이다! 
# [참고] 또한 os.getpid는 시스템의 PID를 가져오는 것임으로 아래 두 경우 모두 parent PID는 동일하다 


# ============1. 동일한 작업을 하는 스레드 생성=============

def foo():
    print('process id', os.getpid())
    print('thread id', threading.get_native_id())

if __name__ == '__main__':  # 현재 모듈(__name__)이 직접실행(__main__)될 때 조건문을 실행해
    print('same_process id', os.getpid())  
    thread1 = threading.Thread(target=foo).start()  # foo()를 실행하는 스레드(thread1~3)를 만들어서 실행해
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()

'''결과 : 동일한 process를 공유하는 각기 다른 thread 이다.
same_process id 41160 
process id 41160
thread id 28592
process id 41160
thread id 16328
process id 41160
thread id 22820
'''


# 시각적으로 실행 순서를 보기 위한 구분선
print("="*30)
'''
구분선이 하나만 생기는 것으로 보아
thread들은 같은 process 과정임을 알 수 있고, 시스템 콜이 반복되지 않아 자원이 낭비되지 않음을 볼 수 있다.
구분선의 위치가 매 실행마다 바뀌는 것으로 보아
매실행마다 프로세스들의 실행속도 차이가 존재함을 알 수 있다.
'''

# ============2. 다른 작업을 하는 스레드 생성=============

def foo():
    print('This is foo', os.getpidㄴ())
    print('thread id', threading.get_native_ids())
    

def bar():
    print('This is bar', os.getpid())
    print('thread id', threading.get_native_id())
    

def baz():
    print('This is baz', os.getpid())
    print('thread id', threading.get_native_id())

if __name__ == '__main__':
    print('diff_process id', os.getpid()) 
    thread4 = threading.Thread(target=foo).start()  
    thread5 = threading.Thread(target=bar).start()  
    thread6 = threading.Thread(target=baz).start()  
    
'''결과
diff_process id 41160
This is foo 41160
thread id 22448
This is bar 41160
thread id 19828
This is baz 41160
thread id 18420
'''   

'''스레드 테스트
의도적으로 foo()에 오타를 주어 error를 발생시켰을 때,
thread4 가 error를 일으켜도 "Exception"하며 프로세스 내의 나머지 스레드를 실행한다.
이는 thread가 각기 다른 실행흐름을 갖기 때문이다.
'''