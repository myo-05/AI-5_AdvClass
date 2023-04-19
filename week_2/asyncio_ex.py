import asyncio
import random
import os
os.system("cls")

async def fetch_data():
    print("데이터를 가져오는 중...")
    await asyncio.sleep(1) # 데이터를 가져오는데 1초가 걸린다고 가정
    return random.randint(1, 100) 

async def main():
    data = await fetch_data()   # 데이터가 들어올 때까지 대기
    print(f"가져온 데이터: {data}")

asyncio.run(main())


'''
파일명을 일반적으로 사용하는 모듈처럼 작성하지 않도록 주의!
파일명을 모듈로 인식해서 의도한 모듈을 실행치 못 할 수 있다!
'''