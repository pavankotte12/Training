select 
	first_name || ' ' || last_name as employee_name,
	extract(year from hire_date)   as hire_year,
	hire_date
from employees;