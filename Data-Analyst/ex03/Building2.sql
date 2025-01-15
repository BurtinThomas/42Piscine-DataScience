SELECT user_id, SUM(price)
FROM customers
Where event_type = 'purchase'
GROUP BY user_id
Having SUM(price) < 225;