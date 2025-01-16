SELECT d.name AS discipline, s.name as student, t.name AS teacher, ROUND(AVG(grade),2) as average_grade
FROM grade g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON g.discipline_id = d.id 
LEFT JOIN teachers t ON d.teacher_id = t.id 
WHERE s.id = 3 AND t.id = 1
GROUP BY discipline
ORDER BY average_grade DESC