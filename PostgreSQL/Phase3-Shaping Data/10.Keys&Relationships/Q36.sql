select * from products
alter table products
add supplier_id int

Update products
set supplier_id = 27
where product_name in ('Laptop', 'Mouse', 'Keyboard')