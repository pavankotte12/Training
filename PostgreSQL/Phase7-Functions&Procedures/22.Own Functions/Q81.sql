create function full_name(first_name text, last_name text)
returns text as $$
begin
	return first || ' ' || last;
end;
$$ Language plpgsql;

select full_name(first_name, last_name) as full_name from employees