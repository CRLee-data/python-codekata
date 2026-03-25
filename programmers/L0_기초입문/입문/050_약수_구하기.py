# 약수 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120897
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 03. 25. 21:33:47

def solution(n):
    return [num for num in range(1, n+1) if n % num == 0]