WITH RankedEmployees AS (
    SELECT
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS salary_rank
    FROM Employee
)
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM RankedEmployees e
JOIN Department d ON e.departmentId = d.id
WHERE e.salary_rank <= 3;