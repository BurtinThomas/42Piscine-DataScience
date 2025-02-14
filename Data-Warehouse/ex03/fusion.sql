CREATE TABLE customers_left_joined_item (
  event_time TIMESTAMP,
  event_type VARCHAR(255),
  product_id SERIAL,
  price DECIMAL,
  user_id SERIAL,
  user_session VARCHAR(36),
  item_category_id VARCHAR(255),
  item_brand VARCHAR(255)
);

INSERT INTO customers_left_joined_item
SELECT customers.event_time, 
  customers.event_type,
  customers.product_id,
  customers.price,
  customers.user_id,
  customers.user_session,
  item.category_id as item_category_id,
  item.brand as item_brand
FROM customers
LEFT JOIN item ON customers.product_id = item.product_id;

drop table customers;

ALTER TABLE customers_left_joined_item
RENAME TO customers;