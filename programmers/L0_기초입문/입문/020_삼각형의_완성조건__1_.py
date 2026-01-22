# 삼각형의 완성조건 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 01. 22. 13:48:41

#if a > b and a > c : a < b+c 
def solution(sides):
    r_sides = sorted(sides, reverse=True)
    a = r_sides[0]
    b = r_sides[1]
    c = r_sides[2]
    if a < b+c : 
        return 1
    else : 
        return 2

