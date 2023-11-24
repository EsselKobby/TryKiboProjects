# Initialize an empty list to store student data
students = []

# Add student records interactively until the user chooses to quit
while True:
    # Get student name
    student_name = input("Enter student name: ")

    # Check if the user wants to quit
    if student_name == "quit":
        break

    # Get student subjects and results
    subjects = {}
    while True:
        subject_name = input("Enter subject name (or 'done' to finish): ")

        # Check if the user has finished entering subjects
        if subject_name == "done":
            break

        subject_result = float(input(f"Enter result for {subject_name}: ")).strip()
        subjects[subject_name] = subject_result

    # Add student data to the list
    students.append({"name": student_name, "subjects": subjects})

# Display student averages
for student in students:
    total_result = 0
    for subject_result in student["subjects"].values():
        total_result += subject_result

    average_result = total_result / len(student["subjects"])
    print(f"Average score for {student['name']}: {average_result}")
