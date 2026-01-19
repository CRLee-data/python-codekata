# 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157340
# 작성자: 이채리
# 작성일: 2026. 01. 19. 11:37:40

-- 코드를 입력하세요
-- 2022-10-16 "대여중", "대여 가능" AS AVAILABILITY, 자동차 ID(내림차순)
-- 반납날짜도 확인
SELECT DISTINCT C1.CAR_ID AS CAR_ID,
    CASE WHEN EXISTS (
    SELECT 1 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY C2
    WHERE C2.CAR_ID = C1.CAR_ID 
    AND C2.START_DATE <= '2022-10-16' 
    AND C2.END_DATE >= '2022-10-16')
    THEN "대여중"
    ELSE "대여 가능" 
    END AS AVAILABILITY
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY C1
ORDER BY 1 DESC;