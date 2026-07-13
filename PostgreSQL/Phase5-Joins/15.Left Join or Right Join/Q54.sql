select d.department_id,	d.department_name,
	count(e.employee_id) as employee_count
from departments d
left join employees e
	on d.department_id = e.department_id
group by d.department_id, d.department_name;