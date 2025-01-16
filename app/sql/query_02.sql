    SELECT d.name AS discipline, s.name as student, ROUND(AVG(grade),2) as average_grade
    FROM grade g
    LEFT JOIN students s ON s.id = g.student_id 
    LEFT JOIN disciplines d ON g.discipline_id = d.id 
    WHERE g.discipline_id = 2
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1