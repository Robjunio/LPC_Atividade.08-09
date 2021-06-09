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

    for i in range(0, 5):
        if i == 0:
            university = University(name= "UEA/EST",
                    department= Department(name=
                            "departament"+str(i),
                                professor= professors[0])
        )
        else:
            university.add_departament(
                Department(name= "departament"+str(i),
                            professor= professors[i])
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
