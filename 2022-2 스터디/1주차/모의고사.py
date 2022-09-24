def solution(answers):
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    ans = []
    
    for i in range(len(answers)):
        if s1[i % 5] == answers[i]: # 배열 반복을 위해 %를 활용해 나머지로 인덱싱
            cnt[0] += 1
        if s2[i % 8] == answers[i]:
            cnt[1] += 1
        if s3[i % 10] == answers[i]:
            cnt[2] += 1
    
    for idx,val in enumerate(cnt): 
        if val == max(cnt): # 최대값이랑 value랑 같으면
            ans.append(idx + 1) # ans에 추가
    
    return ans