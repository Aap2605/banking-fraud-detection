SELECT COUNT(*) FROM fraud_transactions;

SELECT COUNT(*) 
FROM fraud_transactions
WHERE fraud_flag = 1;

SELECT AVG(amount)
FROM fraud_transactions;

SELECT payment_type, COUNT(*)
FROM fraud_transactions
WHERE fraud_flag = 1
GROUP BY payment_type;

SELECT location, COUNT(*)
FROM fraud_transactions
WHERE fraud_flag = 1
GROUP BY location;