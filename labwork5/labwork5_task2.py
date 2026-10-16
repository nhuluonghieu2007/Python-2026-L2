import pandas as pd

# 1. Load both files
students = pd.read_csv('students (1).csv')
scores = pd.read_csv('scores (1).csv')

# 2. Check missing values
print("--- Số lượng giá trị khuyết ở bảng students ---")
print(students.isnull().sum())

print("\n--- Số lượng giá trị khuyết ở bảng scores ---")
print(scores.isnull().sum())

# 3. Fill or remove missing data
students_clean = students.copy()
students_clean['age'] = students_clean['age'].fillna(students_clean['age'].median())
students_clean['GPA'] = students_clean['GPA'].fillna(students_clean['GPA'].mean())

scores_clean = scores.copy()
scores_clean['math'] = scores_clean['math'].fillna(scores_clean['math'].mean())
scores_clean['database'] = scores_clean['database'].fillna(scores_clean['database'].mean())

# 4. Merge the two datasets
merged_df = pd.merge(students_clean, scores_clean, on='student_id')

# 5. Calculate each student's average score
merged_df['average_score'] = merged_df[['python', 'math', 'database']].mean(axis=1)

# 6. Find the top 5 students
top5 = merged_df.sort_values(by='average_score', ascending=False).head(5)
print("\n--- Top 5 sinh viên có điểm trung bình thi cao nhất ---")
print(top5[['student_id', 'name', 'major', 'average_score']])

# 7. Compute average score by major
avg_score_by_major = merged_df.groupby('major')['average_score'].mean()
print("\n--- Điểm thi trung bình theo ngành học ---")
print(avg_score_by_major)