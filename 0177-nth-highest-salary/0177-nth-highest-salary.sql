CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N - 1;
  RETURN (
    select(select distinct salary from Employee where salary = (select distinct(salary) from Employee order by salary desc Limit 1 OFFSET N ))
  );
END