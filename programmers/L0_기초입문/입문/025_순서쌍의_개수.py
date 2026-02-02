# 순서쌍의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120836
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 02. 02. 10:45:30

def solution(n):
    answer = 0
    for i in range(1, n+1) : 
        if n % i == 0 :
            answer += 1
    return answer