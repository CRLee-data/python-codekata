# 가장 큰 수 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 03. 26. 15:26:29

def solution(array):
    answer = sorted(array, reverse=True)
    for n, i in enumerate(array) : 
        if i == answer[0] : 
            return [i, n]
    