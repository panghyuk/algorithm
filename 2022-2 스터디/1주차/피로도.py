from itertools import permutations

def solution(k, dungeons):
    perm = permutations(dungeons,len(dungeons)) # 던전 개수 기준 조합 만들기
    ans = 0
    
    for dungeon in perm:
        tmp = k # k로 초기화
        cnt = 0
        for need,use in dungeon:
            if tmp >= need:
                k -= use
                cnt += 1
        ans = max(ans,cnt)
        
    return ans