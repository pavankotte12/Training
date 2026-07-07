select 
	round(avg(unit_cost),2)     as avg_price,
	min(unit_cost)	   as highest_price,
	max(unit_cost)     as lowest_price
from products;


