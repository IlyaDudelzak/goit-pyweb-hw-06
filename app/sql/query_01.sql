    SELECT s.name as students, ROUND(AVG(grade),2) as average_grade
    FROM grade g
    LEFT JOIN students s ON s.id = g.student_id 
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5