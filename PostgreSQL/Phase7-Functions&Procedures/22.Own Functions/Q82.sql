create function annual_salary(monthly numeric)
returns numeric as $$
begin
return monthly * 12;  
end;
$$ language plpgsql;

select 
	first_name, last_name,
	salary as montly_salary,
	annual_salary(salary) as salary
from employees;