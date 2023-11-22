class Subject:
    def __init__(self, name, credit_hours):
        self.name = name
        self.credit_hours = credit_hours


class SchemeOfStudy:
    def __init__(self):
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)

    def display_scheme(self):
        print("Scheme of Study:")
        for subject in self.subjects:
            print(f"{subject.name} - {subject.credit_hours} credit hours")


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.scheme_of_study = SchemeOfStudy()

    def enroll_subject(self, subject):
        self.scheme_of_study.add_subject(subject)

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        self.scheme_of_study.display_scheme()


class Section:
    def __init__(self, section_id):
        self.section_id = section_id
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_section_info(self):
        print(f"Section ID: {self.section_id}")
        print("Students in this section:")
        for student in self.students:
            student.display_student_info()


class Class:
    def __init__(self, class_id):
        self.class_id = class_id
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def display_class_info(self):
        print(f"Class ID: {self.class_id}")
        print("Sections in this class:")
        for section in self.sections:
            section.display_section_info()


class SchemeOfStudyManager:
    def __init__(self):
        self.classes = []

    def add_class(self, _class):
        self.classes.append(_class)

    def display_scheme_manager_info(self):
        print("Scheme of Study Manager")
        print("Classes managed:")
        for _class in self.classes:
            _class.display_class_info()


# Example Usage:

# Create subjects
math_subject = Subject("Mathematics", 3)
physics_subject = Subject("Physics", 4)
chemistry_subject = Subject("Chemistry", 3)

# Create a scheme of study
scheme_of_study = SchemeOfStudy()
scheme_of_study.add_subject(math_subject)
scheme_of_study.add_subject(physics_subject)
scheme_of_study.add_subject(chemistry_subject)

# Create a student and enroll in subjects
student1 = Student(1, "John Doe")
student1.enroll_subject(math_subject)
student1.enroll_subject(physics_subject)

# Create a section and add a student
section1 = Section("A")
section1.add_student(student1)

# Create a class and add a section
class1 = Class("10th Grade")
class1.add_section(section1)

# Create a Scheme of Study Manager and add a class
manager = SchemeOfStudyManager()
manager.add_class(class1)

# Display information
manager.display_scheme_manager_info()
