SELECT gr.name AS [group], d.name AS discipline, s.name as student, t.name AS teacher, grade, date_of
FROM grade g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON g.discipline_id = d.id 
LEFT JOIN teachers t ON d.teacher_id = t.id 
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE gr.id = 3 AND d.id = 1  
AND date_of = (
	SELECT MAX(date_of)
	FROM grade g
	LEFT JOIN students s ON s.id = g.student_id 
	WHERE s.group_id = 3 AND g.discipline_id = 1
)
ORDER BY grade DESC;