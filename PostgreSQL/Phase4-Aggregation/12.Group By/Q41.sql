select department_id,
	count(*) as number_of_employees
from employees
group by department_id
order by department_id;

	


