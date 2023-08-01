SELECT s.group_id, AVG(g.grade) AS average_grade
FROM Grades g
JOIN Students s ON g.student_name = s.name
JOIN Subjects sub ON g.subject_name = sub.name
WHERE sub.name = 'Subject-1'
GROUP BY s.group_id;