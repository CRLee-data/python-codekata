# 옷가게 할인 받기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 03. 12. 10:32:48

def solution(price):
    answer = 0
    if price >= 500000 : 
        answer = price*0.8
    elif price >= 300000 : 
        answer = price*0.9
    elif price >= 100000 : 
        answer = price*0.95
    else : 
        answer = price
    return int(answer)