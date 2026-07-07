select * from employees;

select first_name, last_name 
as top_level_employee
from employees 
where manager_id is null



