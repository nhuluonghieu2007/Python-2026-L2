from school.domains import students, courses, marks

def list_students():
    print("\nDanh sách sinh viên:")
    for s in students:
        print(f"ID: {s['id']}, Tên: {s['name']}, Ngày sinh: {s['dob']}")

def list_courses():
    print("\nDanh sách môn học:")
    for c in courses:
        print(f"ID: {c['id']}, Tên: {c['name']}")

def show_student_marks():
    if not marks:
        print("Chưa có điểm nào được nhập!")
        return

    print("\nDanh sách môn học hiện có:")
    for c in courses:
        print(f"- ID: {c['id']} | Tên: {c['name']}")

    course_id = input("\nNhập Mã khóa học để xem điểm: ")

    if course_id not in marks:
        print("Mã khóa học không tồn tại hoặc chưa có điểm được nhập!")
        return

    print(f"\n--- BẢNG ĐIỂM KHÓA HỌC {course_id} ---")
    for s in students:
        s_id = s['id']
        s_name = s['name']
        score = marks[course_id].get(s_id, "Chưa có điểm")
        print(f"Sinh viên: {s_name} (ID: {s_id}) - Điểm: {score}")