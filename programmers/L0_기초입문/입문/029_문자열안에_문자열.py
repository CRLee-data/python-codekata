# 문자열안에 문자열
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120908
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 02. 04. 22:37:46

def solution(str1, str2) : 
    return 1 if str2 in str1 else 2
''' if str2 in str1 : 
        return 1
    else :
        return 2'''
