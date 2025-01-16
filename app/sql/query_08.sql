SELECT t.name AS teacher, d.name AS discipline, ROUND(AVG(grade),2) as average_grade
FROM grade g 
LEFT JOIN disciplines d ON g.discipline_id  = d.id 
LEFT JOIN teachers t ON d.teacher_id = t.id 
WHERE t.id = 1
GROUP BY d.id
