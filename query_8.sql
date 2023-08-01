SELECT teacher_name, AVG(grade) AS average_grade
FROM Grades
WHERE teacher_name = 'Teacher_name'
GROUP BY teacher_name;