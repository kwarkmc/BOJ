# 조건을 만족하는 차를 먼저 선별한 후 (서브쿼리), 월별 대여 대수를 구해야 한다 (메인쿼리).

SELECT
    MONTH(START_DATE) AS MONTH,
    CAR_ID,
    COUNT(HISTORY_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    MONTH(START_DATE) BETWEEN 8 AND 10
    # 그냥 CAR_ID 만 WHERE 절에 넣게 되면 해당 CAR_ID의 다른 월의 대여 기록까지 조회하므로 메인쿼리에서도 이를 검사해줘야 한다.
    AND CAR_ID IN (
    SELECT
        CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE
        DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
    GROUP BY CAR_ID
    HAVING COUNT(CAR_ID) >= 5
    )
GROUP BY MONTH, CAR_ID
ORDER BY
    MONTH ASC,
    CAR_ID DESC;
    