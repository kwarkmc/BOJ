SELECT
    COUNT(DISTINCT NAME)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
# 행에서 NULL이 아닌 값을 조건으로 걸고 싶다면 != 가 아닌 IS NOT을 사용해야만 한다.