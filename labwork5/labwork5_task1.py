import pandas as pd

# 1. Load dataset
students = pd.read_csv('students (1).csv')

# 2. Display first 5 rows
print("--- 5 dòng đầu tiên ---")
print(students.head())

# 3. Find number of rows and columns
rows, cols = students.shape
print(f"\nKích thước tập dữ liệu: {rows} dòng, {cols} cột")

# 4. Select name and GPA
print("\n--- Cột Name và GPA ---")
print(students[['name', 'GPA']])

# 5. Find students with GPA >= 3.5
high_gpa = students[students['GPA'] >= 3.5]
print(f"\n--- Sinh viên có GPA >= 3.5 (Tổng: {len(high_gpa)}) ---")
print(high_gpa[['student_id', 'name', 'major', 'GPA']])

# 6. Sort students by GPA (giảm dần)
sorted_students = students.sort_values(by='GPA', ascending=False)
print("\n--- Danh sách sinh viên sắp xếp theo GPA giảm dần ---")
print(sorted_students[['student_id', 'name', 'GPA']].head())

# 7. Find average GPA by major
avg_gpa_major = students.groupby('major')['GPA'].mean()
print("\n--- GPA trung bình theo ngành học ---")
print(avg_gpa_major)
