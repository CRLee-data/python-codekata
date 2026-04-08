# 피자 나눠 먹기 (2)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 04. 08. 14:45:08

def solution(n):
    answer = 0
    answer = (n*6)//GCD(n, 6)
    return answer//6

def GCD(a, b):
    while(b>0):
        a, b = b, a%b
    return a