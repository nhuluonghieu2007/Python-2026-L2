import pandas as pd
import matplotlib.pyplot as plt

# 1. Load tập dữ liệu điểm số
df = pd.read_csv("scores (1).csv")

# -------------------------------------------------------------
# 1. SCATTER PLOT
# -------------------------------------------------------------
plt.figure(figsize=(9, 5))
plt.scatter(df.index, df['math'], label='Math', color='dodgerblue', alpha=0.8)
plt.scatter(df.index, df['python'], label='Python', color='orange', alpha=0.8)
plt.scatter(df.index, df['database'], label='Database', color='mediumseagreen', alpha=0.8)

plt.title("Student Marks Scatter Plot")
plt.xlabel("Student Index")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.savefig("scattered.png")
plt.close()

# -------------------------------------------------------------
# 2. HISTOGRAM (3 SUBPLOTS)
# -------------------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
courses = ['math', 'python', 'database']
colors = ['skyblue', 'salmon', 'lightgreen']

for ax, course, color in zip(axes, courses, colors):
    ax.hist(df[course].dropna(), bins=8, color=color, edgecolor='black')
    ax.set_title(f"{course.capitalize()} Distribution")
    ax.set_xlabel("Score")
    ax.set_ylabel("Frequency")
    ax.grid(True)

plt.tight_layout()
plt.savefig("histo.png")
plt.close()

# -------------------------------------------------------------
# 3. BOX PLOT
# -------------------------------------------------------------
plt.figure(figsize=(8, 5))
df[['math', 'python', 'database']].boxplot()
plt.title("Course Marks Box Plot")
plt.ylabel("Scores")
plt.grid(True)
plt.savefig("box.png")
plt.close()

print("[+] Đã xuất các tệp ảnh: scattered.png, histo.png, box.png")