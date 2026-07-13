select 
	category,
	count(*) as count_of_products,
	Round(Avg(unit_cost),2) as average_price
from products
group by category limit 3


	


