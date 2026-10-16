from school.domains import students, courses, marks

def num_student():
    return int(input("Nhập số học sinh trong lớp: "))

def info_student():
    n = num_student()
    for i in range(n):
        print(f"\n--- Thông tin học sinh thứ {i + 1} ---")
        student_id = input("Nhập ID học sinh: ")
        student_name = input("Nhập tên học sinh: ")
        student_dob = input("Nhập ngày sinh của học sinh: ")
        students.append({
            'id': student_id,
            'name': student_name,
            'dob': student_dob
        })

def num_course():
    return int(input("Nhập số môn học: "))

def info_course():
    m = num_course()
    for i in range(m):
        print(f"\n--- Thông tin môn học thứ {i + 1} ---")
        course_id = input("Nhập ID môn học: ")
        course_name = input("Nhập tên môn học: ")
        courses.append({
            'id': course_id,
            'name': course_name
        })

def input_marks():
    if not courses:
        print("Chưa có khóa học nào được nhập!")
        return
    if not students:
        print("Chưa có sinh viên nào được nhập!")
        return

    print("\nDanh sách môn học hiện có:")
    for c in courses:
        print(f"- ID: {c['id']} | Tên: {c['name']}")

    course_id = input("\nNhập Mã khóa học cần nhập điểm: ")

    course_exists = any(c['id'] == course_id for c in courses)
    if not course_exists:
        print("Mã khóa học không tồn tại!")
        return

    if course_id not in marks:
        marks[course_id] = {}

    print(f"\n--- NHẬP ĐIỂM CHO KHÓA HỌC {course_id} ---")
    for s in students:
        s_id = s['id']
        s_name = s['name']
        score = float(input(f"Nhập điểm cho sinh viên {s_name} (ID: {s_id}): "))
        marks[course_id][s_id] = score