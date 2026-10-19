
# Student Record Management System

def display_student(student):
    print("\n--- Student Record ---")
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")


def update_marks(student, marks):
    student["marks"] = marks
    print("\nMarks updated successfully!")


def main():
    student = {
        "name": "Saheba",
        "roll_number": 101,
        "course": "Python Programming",
        "marks": 85
    }

    display_student(student)

    update_marks(student, 92)

    display_student(student)

    print("\n--- Student Details ---")
    print("Name:", student["name"])
    print("Marks:", student["marks"])


if __name__ == "__main__":
    main()
