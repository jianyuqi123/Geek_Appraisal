import random
import os
import time
while 1:
    os.system('cls')
    A = [0]*10
    C = [0]*10
    for i in range(0,10):
        A[i] = random.randint(65,122)
        while 90 < A[i] < 97:
            A[i] = random.randint(65,122)
            i+=1
    i = 0
    for i in range(0,10):
        A[i] = chr(A[i])
        i+=1
    print(A)
    time_start = time.time()
    B = input()
    time_end = time.time()
    time_c = time_end - time_start
    i = 0
    for i in range(0,10):
        C[i] = B[i:i+1]
        i+=1
    i = 0
    score = 0
    for i in range(0,10):
        if A[i] == B[i]:
                score += 1
    print("score =",score)
    print("timecost =",time_c,"s")
    temp = input("输入1开启下一次游戏,输入其他数字退出")
    if int(temp) == 1:
        continue
    if int(temp) != 1:
        break
print("已退出")