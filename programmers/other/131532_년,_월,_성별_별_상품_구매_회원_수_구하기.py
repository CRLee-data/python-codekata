# 년, 월, 성별 별 상품 구매 회원 수 구하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131532
# 작성자: 이채리
# 작성일: 2026. 01. 19. 13:37:29

-- 코드를 입력하세요
-- 연/월/성별 별, 상품 구매 회원수, 성별 NULL 제외
SELECT YEAR(O.SALES_DATE), MONTH(O.SALES_DATE), U.GENDER, COUNT(DISTINCT U.USER_ID) AS USERS
FROM ONLINE_SALE O
JOIN USER_INFO U
ON O.USER_ID = U.USER_ID
WHERE U.GENDER IS NOT NULL
GROUP BY YEAR(O.SALES_DATE), MONTH(O.SALES_DATE), U.GENDER
ORDER BY 1 ASC, 2 ASC, 3 ASC;
