# 제곱수 판별하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 02. 06. 09:36:26

def solution(n): 
    return (1 if n ** 0.5 == int(n ** 0.5) else 2)

'''
    if n ** 0.5 == int(n ** 0.5) : 
        return 1
    else : 
        return 2
'''