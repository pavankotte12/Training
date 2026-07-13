select
    c.customer_name,
    p.product_name,
    oi.quantity,
    (oi.quantity * oi.unit_price) AS line_total
from customers c
join orders o
    on c.customer_id = o.customer_id
join order_items oi
    on o.order_id = oi.order_id
join products p
    on oi.product_id = p.product_id
where o.order_status = 'Shipped';

select * from customers
SELECT DISTINCT order_status
FROM orders
where order_status = 'Shipped';

SELECT * FROM orders;
SELECT * FROM order_items;
select * from products