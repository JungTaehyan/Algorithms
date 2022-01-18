N = int(input()) #과목 수
score = input().split() #점수

new_score = []
b = 0

#문자열 전부 정수로 바꾸기
for i in range(N):
    score[i] = int(score[i])

max_score = max(score)

#바뀐 정수로 새로운 점수 리스트 만들기
for i in score:
    b = i/max_score*100
    new_score.append(b)
total_score = 0

#평균
for j in new_score:
    total_score += j

avg_score = total_score/N
print(avg_score)

# 문자열 list 정수로 바꾸기 중요함!!