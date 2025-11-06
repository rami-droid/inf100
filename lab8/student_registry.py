import json

def convert_students_to_csv(path, out):
    with open(path, "r") as f:
        content = f.read()
        content = json.loads(content)

    students = content["students"]
    header = []
    csv_list = []
    print(students)
    for item in iter(students[0].items()):
        header.append(item[0])
    csv_list.append(";".join(header))

    for student in students:
        student_string = []
        for item in iter(student.items()):
            student_string.append(item[1])
        student_string = [f"{n}" for n in student_string]
        csv_list.append(";".join(student_string))
    print(header)

    csv_string = "\n".join(csv_list)
    with open(out, "w") as g:
       g.write(csv_string)
    return content

convert_students_to_csv("students.json", "students.csv")
