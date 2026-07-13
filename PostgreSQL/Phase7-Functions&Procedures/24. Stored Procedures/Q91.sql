create procedure give_raise(emp_id integer, pct numeric)
language plpgsql as $$
begin 
	update employees
	set salary = salary * (1 + pct/100)
	where employee_id = emp_id;

	Raise Notice 'Updated salary for employee %', emp_id;
end;
$$;

call give_raise(2,20)


create procedure add_department(name text, loc text)
language plpgsql as $$
begin
 insert into departments(department_name, location)
 values(name, loc);
end;
$$;

call add_department('Sales', 'Hyderabad' )

select * from departments
