select category,
	count(*) as product_count
from products
group by category
having avg(unit_cost)>500

	

	


