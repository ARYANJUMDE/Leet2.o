# Write your MySQL query statement b
select (select salary as SecondHighestSalary from Employee where salary< (select max(salary) from Employee) order by salary desc limit 1) as SecondHighestSalary ;
