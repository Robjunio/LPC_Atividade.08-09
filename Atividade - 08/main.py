from Department import Department
from Professor import Professor
from Subject import Subject
from University import University

if __name__ == '__main__':

    subjects = []
    professors = []

    for i in range(0, 5):
        subjects.append(
            Subject(
                "Subject " + str(i),
                i
            )
        )

    for i in range(0, 5):
        professors.append(
            Professor(
                "Professor " + str(i)
            )
        )
        professors[i].subjects.append(subjects[i])

    university = University(
        name="UEA/EST",
        department=Department(
            name="Tecnologia",
            professor=professors[0]
        )
    )

    print(university.name)
    for department in university.departments:
        print(department.name)
        for professor in department.professors:
            print(professor.name)
            for subject in professor.subjects:
                print(subject.name)
