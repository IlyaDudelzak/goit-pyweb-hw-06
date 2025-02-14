SELECT s.name as student, d.name AS discipline, gr.name AS [group], grade
FROM grade g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON g.discipline_id = d.id 
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE d.id = 1 AND gr.id = 1
ORDER BY grade DESC