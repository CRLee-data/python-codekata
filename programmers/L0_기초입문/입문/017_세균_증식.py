# 세균 증식
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 01. 21. 11:17:44

def solution(n, t):
    answer = 0
    for i in range(1, n+1) : 
        answer = i*2**t
    return answer
