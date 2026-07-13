create function is_top_customer(cust_id integer)
returns boolean as $$
declare 
	order_count integer;
begin 
	select count(*)
	into order_count
	from orders
	where order_id = cust_id;
	
	if order_count > 2 then
		return TRUE;
	else 
		return FALSE;
	end if;
end;
$$ language plpgsql

select 
	customer_id, 
	is_top_customer(customer_id) as is_top_customer
from customers;


 