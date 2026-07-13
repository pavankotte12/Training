select 
	e.first_name || ' ' || e.last_name as employee_name,
	e.salary as employee_salary,
	m.first_name || ' ' || m.last_name as manager_name,
	m.salary as manager_salary
from employees e
join employees m
 on e.manager_id = m.employee_id
where e.salary > m.salary;
	
	


