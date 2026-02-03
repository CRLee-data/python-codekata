# 아이스 아메리카노
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 02. 03. 09:41:56

def solution(money):
    return divmod(money, 5500)
    
''' answer = []
    if money % 5500 == 0 : 
        answer = [money//5500, 0]
    else : 
        answer = [money//5500, money%5500]
    return answer'''