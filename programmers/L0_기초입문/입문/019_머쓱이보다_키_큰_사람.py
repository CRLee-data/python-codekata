# 머쓱이보다 키 큰 사람
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 01. 21. 12:08:23

# [표현식 for 항목 in 리스트 if 조건식]
def solution(array, height):
    x = 0
    for h in array : 
        if h > height : 
            x += 1
    return x
