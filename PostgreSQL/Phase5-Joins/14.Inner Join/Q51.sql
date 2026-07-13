select
	c.customer_name, count(oi.customer_id)
from customers c
join order_items oi
on c.customer_id = oi.customer_id
group by c.customer_name, oi.customer_id;