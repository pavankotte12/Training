select 
	category,
 	count(*) as product_count,
 	avg(unit_cost) as average_price
from products
group by category
having count(*) > 2
	and avg(unit_cost) < 300
order by average_price asc;


