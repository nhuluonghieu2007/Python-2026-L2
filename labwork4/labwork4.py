import os
import zipfile

class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name, credits):
        self.id = course_id
        self.name = name
        self.credits = credits

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}  # Cấu trúc: {(student_id, course_id): mark}

    def load_data(self, dat_filename="students.dat"):
        """Kiểm tra và nạp dữ liệu từ file nén students.dat nếu tồn tại"""
        if os.path.exists(dat_filename):
            print(f"[*] Phát hiện {dat_filename}, đang giải nén và nạp dữ liệu...")
            with zipfile.ZipFile(dat_filename, 'r') as zip_ref:
                zip_ref.extractall(".")

            # Nạp sinh viên từ students.txt
            if os.path.exists("students.txt"):
                self.students.clear()
                with open("students.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        parts = line.strip().split(",")
                        if len(parts) == 3:
                            self.students.append(Student(parts[0], parts[1], parts[2]))

            # Nạp môn học từ courses.txt
            if os.path.exists("courses.txt"):
                self.courses.clear()
                with open("courses.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        parts = line.strip().split(",")
                        if len(parts) == 3:
                            self.courses.append(Course(parts[0], parts[1], int(parts[2])))

            # Nạp điểm từ marks.txt
            if os.path.exists("marks.txt"):
                self.marks.clear()
                with open("marks.txt", "r", encoding="utf-8") as f:
                    for line in f:
                        parts = line.strip().split(",")
                        if len(parts) == 3:
                            self.marks[(parts[0], parts[1])] = float(parts[2])

            print("[+] Nạp dữ liệu thành công!")
        else:
            print("[!] Không tìm thấy students.dat. Khởi tạo dữ liệu mới.")

    def save_data(self, dat_filename="students.dat"):
        """Ghi dữ liệu ra các file txt và nén lại thành students.dat"""
        # Ghi file students.txt
        with open("students.txt", "w", encoding="utf-8") as f:
            for s in self.students:
                f.write(f"{s.id},{s.name},{s.dob}\n")

        # Ghi file courses.txt
        with open("courses.txt", "w", encoding="utf-8") as f:
            for c in self.courses:
                f.write(f"{c.id},{c.name},{c.credits}\n")

        # Ghi file marks.txt
        with open("marks.txt", "w", encoding="utf-8") as f:
            for (s_id, c_id), mark in self.marks.items():
                f.write(f"{s_id},{c_id},{mark}\n")

        # Nén các file thành students.dat
        with zipfile.ZipFile(dat_filename, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            zip_ref.write("students.txt")
            zip_ref.write("courses.txt")
            zip_ref.write("marks.txt")

        print(f"[+] Đã ghi và nén thành công dữ liệu vào {dat_filename}.")
