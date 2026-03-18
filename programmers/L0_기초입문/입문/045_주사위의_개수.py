# 주사위의 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 03. 18. 09:16:12

def solution(box, n):
    a = box[0]//n
    b = box[1]//n
    c = box[2]//n
    return a*b*c