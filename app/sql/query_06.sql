SELECT gr.name as [group] , s.name as student, REVERSE(SUBSTR(REVERSE(s.name), 0, CHARINDEX(' ', REVERSE(s.name)))) AS last_name
FROM students s
LEFT JOIN groups gr ON s.group_id = gr.id 
WHERE group_id = 1
ORDER BY last_name


-- SELECT gr.name as [group] , s.name as student, REVERSE(s.name) AS LN
-- FROM students s
-- LEFT JOIN groups gr ON s.group_id = gr.id 
-- WHERE group_id = 1
-- ORDER BY student
-- -- REVERSE(SUBSTRING(REVERSE(s.name), 0, CHARINDEX('' , REVERSE(s.name))))

