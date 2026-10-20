class Person:
    def __init__(self, person_id, name):
        self._id = person_id        # Encapsulation
        self._name = name

    def list(self):
        """Phương thức Polymorphism cơ sở"""
        print(f"ID: {self._id} | Tên: {self._name}")

class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name)  # Inheritance
        self._dob = dob
        self._marks = {}  # {course_id: mark}

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def set_mark(self, course_id, score):
        self._marks[course_id] = score

    def list(self):
        """Ghi đè (Overriding) đa hình phương thức list()"""
        print(f"SV ID: {self._id} | Họ tên: {self._name} | Ngày sinh: {self._dob}")

class Course:
    def __init__(self, course_id, name, credits):
        self._id = course_id
        self._name = name
        self._credits = credits

    def list(self):
        print(f"Môn ID: {self._id} | Tên môn: {self._name} | Số tín chỉ: {self._credits}")
