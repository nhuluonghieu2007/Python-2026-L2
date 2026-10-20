import os
import pickle
import zipfile
import threading

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def _background_save(self, dat_filename="students.dat"):
        """Tác vụ chạy ngầm trong Background Thread"""
        print("\n[Background Thread] Đang tiến hành lưu và nén dữ liệu qua Pickle...")
        
        # Chuyển đổi dữ liệu sang định dạng dictionary để Pickle an toàn
        s_data = [{"id": s.id, "name": s.name, "dob": s._dob} for s in self.students]
        c_data = [{"id": c._id, "name": c._name, "credits": c._credits} for c in self.courses]

        with open("students.pkl", "wb") as f:
            pickle.dump(s_data, f)
        with open("courses.pkl", "wb") as f:
            pickle.dump(c_data, f)
        with open("marks.pkl", "wb") as f:
            pickle.dump(self.marks, f)

        # Nén các tệp pkl thành tệp .dat
        with zipfile.ZipFile(dat_filename, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
            zip_ref.write("students.pkl")
            zip_ref.write("courses.pkl")
            zip_ref.write("marks.pkl")

        # Dọn dẹp các tệp pkl tạm thời
        for file in ["students.pkl", "courses.pkl", "marks.pkl"]:
            if os.path.exists(file):
                os.remove(file)

        print("[Background Thread] Lưu và nén dữ liệu hoàn tất!")

    def save_data_async(self, dat_filename="students.dat"):
        """Khởi tạo luồng chạy ngầm để lưu dữ liệu"""
        bg_thread = threading.Thread(target=self._background_save, args=(dat_filename,))
        bg_thread.start()
        return bg_thread

    def load_data(self, dat_filename="students.dat"):
        """Giải nén và nạp lại dữ liệu từ Pickle"""
        if os.path.exists(dat_filename):
            print(f"[*] Đang giải nén tệp {dat_filename}...")
            with zipfile.ZipFile(dat_filename, 'r') as zip_ref:
                zip_ref.extractall(".")

            if os.path.exists("students.pkl"):
                with open("students.pkl", "rb") as f:
                    s_data = pickle.load(f)
                    self.students = [Student(s['id'], s['name'], s['dob']) for s in s_data]
                os.remove("students.pkl")

            if os.path.exists("courses.pkl"):
                with open("courses.pkl", "rb") as f:
                    c_data = pickle.load(f)
                    self.courses = [Course(c['id'], c['name'], c['credits']) for c in c_data]
                os.remove("courses.pkl")

            if os.path.exists("marks.pkl"):
                with open("marks.pkl", "rb") as f:
                    self.marks = pickle.load(f)
                os.remove("marks.pkl")

            print("[+] Nạp dữ liệu qua Pickle thành công!")
