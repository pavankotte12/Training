select 
	first_name || ' ' || last_name as employee_name,
	round(salary / 12.0, 2) as monthly_salary
from employees
order by salary desc;