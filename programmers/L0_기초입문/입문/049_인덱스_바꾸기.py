# 인덱스 바꾸기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 03. 24. 11:34:18

def solution(my_string, num1, num2):
    ms = list(my_string)
    ms[num1], ms[num2] = ms[num2], ms[num1]
    answer = ''.join(ms)
    return answer