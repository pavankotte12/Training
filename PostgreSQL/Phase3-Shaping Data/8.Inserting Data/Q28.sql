Insert into customers(customer_id, customer_name, email, phone, city, address, created_at)
values
	(6, 'Mani', 'mani@gmail.com', 9985385932, 'Mumbai', 'karl bagh', default),
	(7, 'Krish', 'krish@gmail.com', 7047398573, 'Vizag', 'jagadamba', default),
	(8, 'Abhishek', 'abhishek@gmail.com', 8948478742,  'Pune', 'pimpari', default);
select * from customers
where city = 'Mumbai'
order by customer_name;