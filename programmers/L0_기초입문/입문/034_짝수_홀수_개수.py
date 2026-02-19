# 짝수 홀수 개수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120824
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 02. 19. 09:13:52

def solution(num_list):
    a = 0
    b = 0    

    for n in num_list :
        if n % 2 == 0 : 
            a += 1
        else : 
            b += 1
            
    return [a, b]