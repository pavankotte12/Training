create function salary_tier(salary numeric)	
returns text as $$
begin
	if salary >= 100000 then
		return 'Senior';
	elsif salary >= 50000 then
		return 'Mid';
	else
		return 'Junior';
	end if;
end;
$$ language plpgsql;

select 
	first_name, last_name,
	salary_tier(salary) as tier
from employees;

