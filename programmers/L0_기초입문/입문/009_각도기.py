# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 이채리
# 작성일: 2026. 01. 19. 14:18:27

def solution(angle):
    if angle == 90 : 
        return 2
    elif angle == 180 : 
        return 4
    elif 0 < angle and angle < 90 : 
        return 1
    else :
        return 3