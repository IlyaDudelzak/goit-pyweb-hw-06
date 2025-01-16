SELECT  d.name AS discipline, gr.name AS [group], ROUND(AVG(grade),2) as average_grade
FROM grade g
LEFT JOIN students s ON s.id = g.student_id 
LEFT JOIN disciplines d ON g.discipline_id = d.id 
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE g.discipline_id = 2
GROUP BY gr.id 
ORDER BY average_grade DESC
