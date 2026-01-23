# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 01. 23. 10:56:46

def solution(s1, s2) : 
    return len([i for i in s1 if i in s2])
