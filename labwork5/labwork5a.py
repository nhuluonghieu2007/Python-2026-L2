import os
import zipfile
import pickle
import pandas as pd

# --- CÁC LỚP ĐỐI TƯỢNG (DOMAINS) ---
class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits


# --- HỆ THỐNG QUẢN LÝ SINH VIÊN (LABWORK 5A) ---
class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}  # Cấu trúc: {(student_id, course_id): score}

    # 1. GHI FILE TXT & NÉN TỆP DAT
    def save_and_compress(self, dat_filename="students.dat"):
        with open("students.txt", "w", encoding="utf-8") as f:
            for s in self.students:
                f.write(f"{s.student_id},{s.name},{s.dob}\n")

        with open("courses.txt", "w", encoding="utf-8") as f:
            for c in self.courses:
                f.write(f"{c.course_id},{c.name},{c.credits}\n")

        with open("marks.txt", "w", encoding="utf-8") as f:
            for (s_id, c_id), score in self.marks.items():
                f.write(f"{s_id},{c_id},{score}\n")

        with zipfile.ZipFile(dat_filename, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            zip_ref.write("students.txt")
            zip_ref.write("courses.txt")
            zip_ref.write("marks.txt")
        print(f"[+] Đã lưu và nén dữ liệu thành công vào {dat_filename}.")

    # 2. LƯU & TẢI BẰNG PICKLE
    def save_with_pickle(self, pickle_filename="data.pkl"):
        data = {
            "students": self.students,
            "courses": self.courses,
            "marks": self.marks
        }
        with open(pickle_filename, "wb") as f:
            pickle.dump(data, f)
        print(f"[+] Đã lưu dữ liệu bằng Pickle vào {pickle_filename}.")

    def load_with_pickle(self, pickle_filename="data.pkl"):
        if os.path.exists(pickle_filename):
            with open(pickle_filename, "rb") as f:
                data = pickle.load(f)
                self.students = data["students"]
                self.courses = data["courses"]
                self.marks = data["marks"]
            print(f"[+] Nạp dữ liệu từ tệp Pickle {pickle_filename} thành công.")

    # 3. EXTRA: XUẤT CSV VÀ TRUY VẤN BẰNG PANDAS
    def export_to_csv(self):
        s_data = [{"student_id": s.student_id, "name": s.name, "dob": s.dob} for s in self.students]
        c_data = [{"course_id": c.course_id, "name": c.name, "credits": c.credits} for c in self.courses]
        m_data = [{"student_id": k[0], "course_id": k[1], "mark": v} for k, v in self.marks.items()]

        pd.DataFrame(s_data).to_csv("students.csv", index=False)
        pd.DataFrame(c_data).to_csv("courses.csv", index=False)
        pd.DataFrame(m_data).to_csv("marks.csv", index=False)
        print("[+] Đã xuất dữ liệu ra 3 tệp: students.csv, courses.csv, marks.csv.")

    def run_query(self, condition_str):
        """Hàm truy vấn trên Pandas DataFrame sinh viên dựa theo điều kiện nhập vào"""
        if not os.path.exists("students.csv"):
            self.export_to_csv()

        # Nạp CSV vào DataFrame của Pandas (Po/pd)
        df_students = pd.read_csv("students.csv")
        print(f"\n--- Thực thi truy vấn: {condition_str} ---")
        try:
            result = df_students.query(condition_str)
            print(result if not result.empty else "Không tìm thấy kết quả phù hợp.")
        except Exception as e:
            print(f"Lỗi cú pháp điều kiện truy vấn: {e}")


# --- DEMO THỰC THI CHƯƠNG TRÌNH ---
if __name__ == "__main__":
    system = StudentManagementSystem()

    # Thêm dữ liệu mẫu
    system.students.append(Student("S001", "Mr. Volunteers", "2002-01-01"))
    system.students.append(Student("S002", "Alice", "2003-05-12"))
    system.courses.append(Course("C001", "Python Programming", 3))
    system.marks[("S001", "C001")] = 18.5

    # 1. Lưu & Nén dữ liệu (.txt và .dat)
    system.save_and_compress()

    # 2. Thực hành lưu qua Pickle
    system.save_with_pickle()

    # 3. Xuất CSV và chạy hàm truy vấn Pandas
    system.export_to_csv()
    
    # Truy vấn thử nghiệm theo yêu cầu đề bài
    system.run_query('name == "Mr. Volunteers"')