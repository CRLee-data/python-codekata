# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 01. 21. 11:47:43

def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]