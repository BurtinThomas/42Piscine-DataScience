CREATE TABLE IF NOT EXISTS customers (
    event_time TIMESTAMP,
    event_type VARCHAR(255),
    product_id SERIAL,
    price DECIMAL,
    user_id SERIAL,
    user_session VARCHAR(36)
);

COPY customers (event_time, event_type, product_id, price, user_id, user_session)
FROM '../subject/customer/data_2023_feb.csv'
DELIMITER ','
CSV HEADER;

INSERT INTO customers
SELECT * FROM data_2022_dec
UNION
SELECT * FROM data_2022_nov
UNION
SELECT * FROM data_2022_oct
UNION
SELECT * FROM data_2023_jan;
