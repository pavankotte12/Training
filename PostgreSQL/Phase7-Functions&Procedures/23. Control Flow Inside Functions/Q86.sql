create function department_headcount(dept_id integer)
returns integer as $$
declare 
	emp_count integer;
begin 
	select count(*)
	into emp_count
	from employees
	where department_id = dept_id;

	return emp_count;
end;
$$ language plpgsql;


select 
	department_id, department_name,
	department_headcount(department_id) as headcount
from departments;

