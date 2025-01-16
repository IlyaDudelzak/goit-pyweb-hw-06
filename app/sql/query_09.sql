SELECT  s.name as student, d.name AS discipline
FROM grade g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON g.discipline_id = d.id 
WHERE s.id = 3
GROUP BY discipline
ORDER BY discipline