SELECT student_name, grade
FROM Grades
WHERE subject_name = 'Subject-1' AND student_name IN (SELECT name FROM Students WHERE group_id = 1);