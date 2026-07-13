create procedure restock_product(prod_id integer, new_price numeric)
language plpgsql as $$
begin 
 update products
 set unit_cost = new_price
 where product_id = prod_id;

 Raise Notice 'Product with ID % price updated successfully.', prod_id;
end;
$$;

call restock_product(5,99)