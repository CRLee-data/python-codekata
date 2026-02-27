# 짝수는 싫어요
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 02. 27. 09:08:06

def solution(n):
    return [num for num in range(1, n+1) if num % 2 == 1]