from Department import Department
from Professor import Professor
from Subject import Subject
from University import University


def instantiate_objects():
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
        subjects[i].professors.append(professors[i])

    university = University(
        name="UEA/EST",
        department=Department(
            name="Tecnologia",
            professor=professors[0]
        )
    )
    university.add_departament(
        Department(
            name="Ciências Humanas",
            professor=professors[1]
        )
    )
    university.add_departament(
        Department(
            name="Ciências Naturais",
            professor=professors[2]
        )
    )

    return university


if __name__ == '__main__':
    university = instantiate_objects()

    print(f"Universidade: {university.name}")
    for department in university.departments:
        print('\n' + department.name)
        for professor in department.professors:
            print(professor.name)
            for subject in professor.subjects:
                print(subject.name)
