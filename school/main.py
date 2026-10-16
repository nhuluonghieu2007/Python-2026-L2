import school

def main():
    # Nhập dữ liệu ban đầu
    school.info_student()
    school.info_course()
    school.input_marks()

    # Hiển thị kết quả
    school.list_students()
    school.list_courses()
    school.show_student_marks()

if __name__ == "__main__":
    main()