select 
	category,
	Round(Avg(unit_cost),2) as average_price
from products
group by category
order by category;

	


