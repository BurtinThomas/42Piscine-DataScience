SELECT user_id, COUNT(*) AS purchases
FROM customers
Where event_type = 'purchase'
Group BY user_id
Having COUNT(*) < 30
ORDER BY purchases DESC;