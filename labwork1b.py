student = []
course = []
marks = {}

def num_student():
    return int(input("Nhap so hoc sinh trong lop: "))

def info_student():
    n = num_student()
    for i in range(n):
        print(f"\n--- Thong tin hoc sinh thu {i + 1} ---")
        Student_ID = input("Nhap ID hoc sinh: ")
        Student_Name = input("Nhap ten hoc sinh: ")
        Student_DoB = input("Nhap ngay sinh cua hoc sinh: ")
        student.append({
            'id': Student_ID,
            'name': Student_Name,
            'dob': Student_DoB
        })

def num_course():
    return int(input("Nhap so mon hoc: "))

def info_course():
    m = num_course()
    for i in range(m):
        print(f"\n--- Thong tin mon hoc thu {i + 1} ---")
        Course_ID = input("Nhap ID mon hoc: ")
        Course_Name = input("Nhap ten mon hoc: ")
        course.append({
            'id': Course_ID,
            'name': Course_Name
        })

def input_marks():
    if not course:
        print("Chưa có khóa học nào được nhập!")
        return
    if not student:
        print("Chưa có sinh viên nào được nhập!")
        return

    print("\nDanh sách môn học hiện có:")
    for c in course:
        print(f"- ID: {c['id']} | Tên: {c['name']}")

    Course_ID = input("\nNhập Mã khóa học cần nhập điểm: ")

    course_exists = any(c['id'] == Course_ID for c in course)
    if not course_exists:
        print("Mã khóa học không tồn tại!")
        return

    if Course_ID not in marks:
        marks[Course_ID] = {}

    print(f"\n--- NHẬP ĐIỂM CHO KHÓA HỌC {Course_ID} ---")
    for s in student:
        s_id = s['id']
        s_name = s['name']
        score = float(input(f"Nhập điểm cho sinh viên {s_name} (ID: {s_id}): "))
        marks[Course_ID][s_id] = score

info_student()
info_course()
input_marks()

print("\nBảng điểm vừa nhập:", marks)

def list_students():
    print("\nDanh sách sinh viên:")
    for s in student:
        print(f"ID: {s['id']}, Tên: {s['name']}, Ngày sinh: {s['dob']}")

def list_courses():
    print("\nDanh sách môn học:")
    for c in course:
        print(f"ID: {c['id']}, Tên: {c['name']}")

def show_student_marks():
    if not marks:
        print("Chưa có điểm nào được nhập!")
        return

    print("\nDanh sách môn học hiện có:")
    for c in course:
        print(f"- ID: {c['id']} | Tên: {c['name']}")

    Course_ID = input("\nNhập Mã khóa học để xem điểm: ")

    if Course_ID not in marks:
        print("Mã khóa học không tồn tại hoặc chưa có điểm được nhập!")
        return

    print(f"\n bảng điểm khóa học {Course_ID} ")
    for s in student:
        s_id = s['id']
        s_name = s['name']
        score = marks[Course_ID].get(s_id, "Chưa có điểm")
        print(f"Sinh viên: {s_name} (ID: {s_id}) - Điểm: {score}")
