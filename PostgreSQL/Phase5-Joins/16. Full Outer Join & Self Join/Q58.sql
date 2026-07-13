select d.department_name,
	p.project_name,
	d.department_id,
	p.project_id
from departments d
full outer join projects p
on d.department_id = p.department_id

