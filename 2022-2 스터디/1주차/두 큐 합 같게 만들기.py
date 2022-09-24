from collections import deque # 그냥 큐로 풀었더니 시간 초과 & Error

def solution(queue1, queue2):
    ans = 0
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    q1 = sum(dq1)
    q2 = sum(dq2)
    l_max = len(dq1) * 4 # 2 곱해주면 테스트 케이스 1에서 틀림
    
    # while 반복문에서 sum 함수 계속 사용하면 시간초과
    while True:
        if q1 > q2:
            tmp = dq1.popleft() # dq1의 맨 왼쪽 값 빼서
            dq2.append(tmp) # dq2 맨 뒤에 추가

            q1 -= tmp # q1에서 tmp 값 빼기
            q2 += tmp # q2에서 tmp 값 더하기
            ans += 1
            
        elif q1 < q2:
            tmp = dq2.popleft()
            dq1.append(tmp)
            q1 += tmp
            q2 -= tmp
            ans += 1
        else:
            break
        
        if ans == l_max:
            ans = -1
            break
    
    return ans