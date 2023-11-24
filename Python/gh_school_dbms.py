class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}

    def add_result(self, subject, result):
        self.subjects[subject] = result

    def get_average(self):
        total = 0
        for result in self.subjects.values():
            total += result
        return total / len(self.subjects)


class ResultsManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def add_subject(self, subject_name):
        if subject_name not in self.subjects_list:
            self.subjects_list.append(subject_name)

    def add_result(self, student_name, subject_name, result):
        student = self.get_student_by_name(student_name)
        if student:
            student.add_result(subject_name, result)
            print(f"Result added successfully for {student_name} in {subject_name}.")
        else:
            print(f"Student {student_name} not found.")

    subjects_list = []


def main():
    # Initialize a results manager
    results_manager = ResultsManager()

    while True:
        # Get user input for action
        action = input(
            "Choose an action (add student, add subject, add result, average, quit): "
        )

        # Handle adding a new student
        if action == "add student":
            student_name = input("Enter student name: ")
            student = Student(student_name)
            results_manager.add_student(student)
            print(f"Student {student_name} added successfully.")

        # Handle adding a new subject
        elif action == "add subject":
            subject_name = input("Enter subject name: ")
            results_manager.add_subject(subject_name)
            print(f"Subject {subject_name} added successfully.")

        # Handle adding a result
        elif action == "add result":
            student_name = input("Enter student name: ")
            subject_name = input("Enter subject name: ")
            result = float(input("Enter result: "))
            results_manager.add_result(student_name, subject_name, result)
            print(f"Result added successfully for {student_name} in {subject_name}.")

        # Calculate and display average
        elif action == "average":
            student_name = input("Enter student name: ")
            student = results_manager.get_student_by_name(student_name)
            if student:
                average = student.get_average()
                print(f"Average score for {student_name}: {average}")
            else:
                print(f"Student {student_name} not found.")

        # Exit the program
        elif action == "quit":
            print("Exiting program...")
            break

        else:
            print("Invalid action. Please choose from the available options.")


if __name__ == "__main__":
    main()
