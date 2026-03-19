# 문자열 정렬하기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 03. 19. 11:45:35

def solution(my_string):
    answer = []
    for n in my_string : 
        if n.isdigit() : 
            answer.append(int(n))
            answer.sort()
    return answer