SELECT student_name, AVG(grade) AS average_grade
FROM Grades
WHERE subject_name = 'Subject-1'
GROUP BY student_name
ORDER BY average_grade DESC
LIMIT 1;