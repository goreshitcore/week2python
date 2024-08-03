# Your student data
import pandas as pd

student_data = {
    'student_name': ["Alice", "Bob", "Charlie", "David", "Eva", "Fiona", "George"],
    'age': [21, 19, 22, 23, 19, 24, 20],
    'course': ["Computer Science", "Engineering", "Psychology", "History", "Biology", "Business Administration", "Physics"],
    'grade': [85, 92, 78, 65, 40, 73, 35]
}
df = pd.DataFrame(student_data)
failed_students = df[df['grade'] < 60]

print(failed_students)
