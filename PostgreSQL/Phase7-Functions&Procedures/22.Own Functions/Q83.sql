create function discounted_price(price numeric, discount_pct numeric)
returns numeric as $$
begin
	return price - (price * discount_pct /100);
end;
$$ language plpgsql;

select 
	product_name, unit_cost, 
	round(discounted_price(unit_cost, 15),2) as discounted_price
from products;
	
	