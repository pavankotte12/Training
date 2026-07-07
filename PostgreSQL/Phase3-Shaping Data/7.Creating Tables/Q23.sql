Alter table suppliers 
alter column city set not null;

select * from suppliers
Insert into suppliers(supplier_id, supplier_name, city)
values
	(1, 'kotte', null);

--  null value in column "city" of relation "suppliers" violates not-null constraint
--Failing row contains (1, kotte, null). 

