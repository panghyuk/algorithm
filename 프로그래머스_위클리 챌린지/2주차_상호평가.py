# level 2
scores = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
          [24, 90, 94, 75, 65]]


def solution(scores):
    answer = ''
    for j in range(len(scores)):
        num_list = []
        for i in range(len(scores)):
            num_list.append(scores[i][j])

        if num_list[j] == min(num_list) and num_list.count(num_list[j]) == 1:
            del num_list[j]
        elif num_list[j] == max(num_list) and num_list.count(num_list[j]) == 1:
            del num_list[j]

        grade = sum(num_list) / len(num_list)

        if grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer += 'B'
        elif grade >= 70:
            answer += 'C'
        elif grade >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer
