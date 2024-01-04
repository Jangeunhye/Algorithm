SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH,COUNT(DISTINCT(ONLINE_SALE.USER_ID)) AS PUCHASED_USERS, 
ROUND(COUNT(DISTINCT(ONLINE_SALE.USER_ID))/(SELECT COUNT(DISTINCT(USER_ID))FROM USER_INFO WHERE YEAR(JOINED)=2021),1)
FROM USER_INFO 
RIGHT JOIN ONLINE_SALE
ON USER_INFO.USER_ID =  ONLINE_SALE.USER_ID
WHERE YEAR(JOINED) = 2021
GROUP BY YEAR(SALES_DATE),MONTH(SALES_DATE)
ORDER BY SALES_DATE