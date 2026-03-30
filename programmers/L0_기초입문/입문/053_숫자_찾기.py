# 숫자 찾기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 03. 30. 10:35:20

def solution(num, k):
    return str(num).find(str(k)) + 1 if str(k) in str(num) else -1
            