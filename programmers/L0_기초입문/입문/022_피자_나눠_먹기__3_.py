# 피자 나눠 먹기 (3)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 01. 22. 23:22:48

# 
def solution(slice, n):
    return (n//slice) + (1 if n % slice > 0 else 0)