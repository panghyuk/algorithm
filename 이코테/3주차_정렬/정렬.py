# 선택 정렬
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
    min_idx = i # 가장 작은 원소의 인덱스
    for j in range(i+1,len(arr)):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i] # 스왑

print(arr)


# 삽입 정렬
arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(1,len(arr)): 
    for j in range(i,0,-1): # 인덱스 i부터 1까지 감소하며 반복
        if arr[j] < arr[j-1]: # 한 칸씩 왼쪽으로 이동
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else: # 자기보다 작은 데이터를 만나면 멈춤
            break
print(arr)


# 퀵 정렬 1
arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr,start,end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while (left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and arr[left] <= arr[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and arr[right] >= arr[pivot]):
            right -= 1
        if (left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
    # 분할 이휴 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)

quick_sort(arr, 0, len(arr)-1)
print(arr)


# 퀵 정렬 2
array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # 피벗은 첫 번째 원소
    tail = arr[1:] # 피벗을 제외한 리스트

    left = [x for x in tail if x <= pivot]
    right= [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))


# 계수 정렬
# 모든 원소의 값이 0보다 크거나 같다고 가정
arr = [7,5,9,0,1,3,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값 0으로 초기화)
cnt = [0] * (max(arr)+1)

for i in range(len(arr)):
    cnt[arr[i]] += 1 # 각 데이터에 해당하는 인덱스 값 증가

for j in range(len(cnt)): # 리스트에 기록된 정렬 정보 확인
    for k in range(cnt[j]):
        print(j, end = ' ')