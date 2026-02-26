# 중앙값 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 02. 27. 00:09:05

def solution(array):
    array.sort()  
    n = len(array)
    mid = n // 2
    return array[mid]
