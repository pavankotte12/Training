Alter table suppliers
add constraint fk_supplier_id
Foreign Key (supplier_id)
References suppliers(supplier_id)
select * from suppliers