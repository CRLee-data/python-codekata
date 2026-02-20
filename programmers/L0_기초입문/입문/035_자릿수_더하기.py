# 자릿수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 02. 20. 15:39:49

def solution(n):
    return sum(int(num) for num in str(n))