select e.first_name|| ' ' || e.last_name as employee_name,
	m.manager_id 
from employees e
left join employees m
	on e.manager_id = m.manager_id;

-- Manager name is not availble in the table so replaced manager_name with manager_id


