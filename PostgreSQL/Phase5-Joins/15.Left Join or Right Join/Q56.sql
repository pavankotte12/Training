select c.customer_name, c.city
from customers c
left join orders o
	on c.customer_id = o.customer_id
where o.order_id is null
order by c.customer_name asc;




