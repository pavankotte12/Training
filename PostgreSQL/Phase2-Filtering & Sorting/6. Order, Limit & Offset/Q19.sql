select * from employees;

select first_name, last_name,salary, department_id 
from employees 
where department_id in (1)
and salary > 50000
order by salary Desc 
limit 2


