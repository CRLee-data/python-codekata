# 암호 해독
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120892
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 03. 23. 11:14:00

def solution(cipher, code):
    answer = ''
    for n, i in enumerate(cipher) : 
        if (n+1) % code == 0 : 
            answer += i
    return answer