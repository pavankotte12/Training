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

