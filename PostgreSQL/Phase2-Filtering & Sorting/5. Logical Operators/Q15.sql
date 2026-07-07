select * from departments;

select * from employees;

select first_name, last_name, salary, department_id from employees
where department_id in (1,2)
and salary > 55000
and hire_date > '2020-01-01' 



